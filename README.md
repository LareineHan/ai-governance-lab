🛡️ AI Governance & Security Lab
Self-Initiated Research on Data Privacy & Policy Enforcement for LLMs
📝 Project Motivation
As a student passionate about Information Security and a contributor at the AI Hub, I initiated this project to bridge the gap between AI innovation and data protection.

I wanted to move beyond theoretical knowledge and understand the architectural challenges of securing Large Language Models (LLMs). This project is the result of my self-motivated research into how organizations can implement "Guardrails" to prevent the leakage of sensitive data (PII) and credentials during AI interactions.

🏗️ Project Structure
To understand modular design and policy management, I structured the project as follows:

security_ai.py: The core Flask application that handles the AI service logic and integrates the security layer.

conditions.py: A dedicated security engine class (AISecurityManager) that executes scanning and detection logic.

policy.json: A decoupled policy configuration file for managing security rules (SSN, Passport, Secrets, etc.) without altering the source code.

🔍 Core Learning Objectives
Through this project, I explored several key domains of Information Security:

DLP (Data Loss Prevention): Learning how to intercept and scan real-time traffic for sensitive US-based PII (SSN, Passport numbers).

Secrets Management: Identifying accidental exposure of API keys, tokens, and private keys within prompts.

Governance as Code: Implementing a system where security policies are managed through JSON, mimicking enterprise-level policy management.

Audit & Compliance: Building an audit trail using SQLite to understand how security incidents are recorded and monitored.

🛠️ Security Policy Overview (policy.json)
The system follows a "Deny by Default" or "Scan then Send" approach. Key detection patterns include:

US PII: Social Security Numbers, Passport Numbers, and Phone patterns.

Credentials: Regex-based detection for API Keys and Auth Secrets.

Dangerous Keywords: Filtering prompts related to unauthorized access or cyber threats.

🚀 How to Run the Lab
Set up your Gemini API Key as an environment variable.

Run python security_ai.py.

Monitor real-time security logs at http://localhost:8080.

💡 Reflection
This is an ongoing research project. My goal is to continue evolving this lab by exploring more advanced topics like Contextual Masking (Redaction) and Adversarial Prompt Testing (Red Teaming) to further my expertise in AI Security.