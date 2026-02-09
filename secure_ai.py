from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime
import os
import re
from google import genai
from google.genai import types
from conditions import AISecurityManager

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# --- [AI Governance: Security Manager] ---


security_mgr = AISecurityManager()

# --- [Gemini API Setup] ---
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version='v1alpha')
)
MODEL_NAME = "models/gemini-3-flash-preview"

# --- [Database Logic] ---
def init_db():
    with sqlite3.connect('ai_log.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS logs
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         user TEXT, question TEXT, status TEXT, time DATETIME)''')
        conn.commit()

def save_log(user, question, status):
    with sqlite3.connect('ai_log.db') as conn:
        conn.execute("INSERT INTO logs (user, question, status, time) VALUES (?, ?, ?, ?)",
                     (user, question, status, datetime.now()))

# --- [Routes] ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['GET'])
def ask():
    user = request.args.get('user', 'anonymous')
    question = request.args.get('q', '')

    if not question:
        return jsonify({"error": "Question is empty"}), 400

    # 1. 보안 스캔 실행
    scan_result = security_mgr.scan(question)
    
    if scan_result["is_blocked"]:
        save_log(user, question, f"BLOCKED: {scan_result['reason']}")
        # 보안 위반 시 403 에러와 사유 반환
        return jsonify({
            "answer": f"보안 위반: {scan_result['reason']}",
            "blocked": True,
            "reason": scan_result['reason']
        }), 403

    # 2. 안전할 경우 AI 호출
    try:
        response = client.models.generate_content(model=MODEL_NAME, contents=question)
        answer = response.text.strip()
        save_log(user, question, "SUCCESS")
        return jsonify({"answer": answer, "blocked": False})
    except Exception as e:
        return jsonify({"answer": f"API Error: {str(e)}", "blocked": False}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)

@app.route('/admin/logs')
def view_logs():
    with sqlite3.connect('ai_log.db') as conn:
        conn.row_factory = sqlite3.Row # 결과를 딕셔너리 형태로 받기 위해
        cursor = conn.execute("SELECT * FROM logs ORDER BY time DESC")
        logs = cursor.fetchall()
    
    # 간단한 HTML 테이블로 출력
    html = """
    <h2>🔒 Security Audit Logs</h2>
    <table border="1" style="width:100%; border-collapse: collapse;">
        <tr style="background-color: #eee;">
            <th>ID</th><th>User</th><th>Question</th><th>Status</th><th>Time</th>
        </tr>
    """
    for log in logs:
        # 차단된 로그는 빨간색으로 표시 (거버넌스 강조)
        color = "red" if "BLOCKED" in log['status'] else "black"
        html += f"<tr style='color: {color}'>"
        html += f"<td>{log['id']}</td><td>{log['user']}</td><td>{log['question']}</td><td>{log['status']}</td><td>{log['time']}</td>"
        html += "</tr>"
    html += "</table><br><a href='/'>Back to Dashboard</a>"
    return html