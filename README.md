# 🛡️ AI Governance & Security Lab
### *Self-Initiated Research on Data Privacy & Policy Enforcement for LLMs*

## 📝 Project Motivation
As a student passionate about **Information Security** and a contributor at the **AI Hub**, I initiated this project to bridge the gap between AI innovation and data protection. 

I wanted to move beyond theoretical knowledge and understand the architectural challenges of securing Large Language Models (LLMs). This project is the result of my self-motivated research into how organizations can implement "Guardrails" to prevent the leakage of sensitive data (PII) and credentials during AI interactions.

---

## 🏗️ Project Structure
To understand modular design and policy management, I structured the project into specialized components:

* **`security_ai.py`**: The core Flask application that handles the AI service logic and integrates the security layer.
* **`conditions.py`**: A dedicated security engine class (`AISecurityManager`) that executes scanning and detection logic.
* **`policy.json`**: A decoupled policy configuration file for managing security rules (SSN, Passport, Secrets, etc.) without altering the source code.
* **`templates/index.html`**: A real-time security dashboard for monitoring and testing.

---

## 🔍 Core Learning Objectives
Through this project, I explored several key domains of Information Security:

1.  **DLP (Data Loss Prevention)**: Implementing real-time traffic scanning for sensitive US-based PII such as Social Security Numbers (SSN) and Passport numbers.
2.  **Secrets Management**: Identifying accidental exposure of API keys, tokens, and private keys within user prompts.
3.  **Governance as Code**: Implementing a system where security policies are managed through a centralized JSON configuration, mimicking enterprise-level policy management.
4.  **Audit & Compliance**: Building an automated audit trail using SQLite to understand how security incidents are recorded for forensic analysis.

---

## 🛠️ Security Policy Overview (`policy.json`)
The system follows a **"Scan-then-Send"** architecture. Key detection patterns calibrated for US compliance include:

* **US PII**: Social Security Numbers (SSN), Passport Numbers, and US Phone formats.
* **Sensitive Data**: Credit Card patterns and Private RSA Keys.
* **Credentials**: Regex-based detection for API Keys and Auth Secrets.
* **Policy Enforcement**: Filtering prompts related to unauthorized access or cyber threats.

---

## 🚀 Getting Started (Codespaces)

1.  **Set Environment Variable**:
    ```bash
    export GEMINI_API_KEY='your_api_key_here'
    ```
2.  **Run the Application**:
    ```bash
    python security_ai.py
    ```
3.  **Access the Lab**:
    Open the forwarded port (default: `8080`) to access the **Security Dashboard**.

---

## 💡 Future Roadmap
This is an ongoing research project. My goal is to continue evolving this lab by exploring:
* **Data Masking/Redaction**: Automatically obfuscating PII instead of just blocking.
* **Adversarial Prompt Testing**: Researching "Prompt Injection" attacks and defensive strategies.
* **NIST AI RMF Alignment**: Mapping security logs to international AI risk management frameworks.

---

### 👨‍💻 About the Author
I am a student researcher focused on the intersection of **
