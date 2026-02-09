import re
import json
import os

class AISecurityManager:
    def __init__(self, policy_file='policy.json'):
        self.policy_file = policy_file
        self.load_policy()

    def load_policy(self):
        if os.path.exists(self.policy_file):
            with open(self.policy_file, 'r', encoding='utf-8') as f:
                self.policy = json.load(f)
        else:
            raise FileNotFoundError(f"Policy file {self.policy_file} not found!")

    def scan(self, text):
        detected_items = []
        is_blocked = False

        # 1. Patterns (SSN, Phone, Keys, etc.)
        for name, pattern in self.policy['patterns'].items():
            if re.search(pattern, text):
                detected_items.append(name)
                is_blocked = True

        # 2. Keywords
        if any(kw in text.lower() for kw in self.policy['banned_keywords']):
            detected_items.append("Banned Content")
            is_blocked = True

        reason = f"Violation: {', '.join(detected_items)}" if is_blocked else "Safe"
        return {
            "is_blocked": is_blocked,
            "reason": reason,
            "system_msg": self.policy['system_message']
        }