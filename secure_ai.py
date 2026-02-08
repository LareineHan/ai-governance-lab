from flask import Flask, request, jsonify  
import sqlite3  
from datetime import datetime  
import os  

app = Flask(__name__)  

# DB 테이블 만들기 (처음 한 번만 실행됨)
def init_db():  
    conn = sqlite3.connect('ai_log.db')  
    conn.execute('''CREATE TABLE IF NOT EXISTS logs 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     user TEXT, 
                     question TEXT, 
                     time DATETIME)''')  
    conn.commit()  
    conn.close()  

# 로그 저장 함수
def save_log(user, question):  
    conn = sqlite3.connect('ai_log.db')  
    conn.execute("INSERT INTO logs (user, question, time) VALUES (?, ?, ?)", 
                 (user, question, datetime.now()))  
    conn.commit()  
    conn.close()  

# 메인 엔드포인트: /ask 로 들어오는 요청 처리
@app.route('/ask', methods=['GET'])  
def ask():  
    user = request.args.get('user')          # ?user=이름 이런 식으로 전달
    q = request.args.get('q')                # ?q=질문내용
    if not user or not q:
        return jsonify({"error": "user와 q 파라미터가 필요합니다"}), 400
    
    # 로그 저장 (가장 핵심!)
    save_log(user, q)
    
    # 여기서는 실제 AI 호출 대신 그냥 에코로 답변 (테스트용)
    answer = f"AI가 답변합니다: {q}"   # 나중에 Grok이나 다른 API로 바꿀 부분
    
    return jsonify({"answer": answer, "logged": True})

# 서버 시작 전에 DB 초기화
if __name__ == '__main__':
    init_db()               # 프로그램 시작 시 DB 테이블 자동 생성
    app.run(host='0.0.0.0', port=8080, debug=True)