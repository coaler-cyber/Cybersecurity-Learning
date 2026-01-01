class SecurityPolicy:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    def check_compliance(self, user_action):
        for rule in self.rules:
            if rule.lower() in user_action.lower():
                print(f"✅ Action '{user_action}' complies with {self.name}")
                return True
        print(f"❌ Action '{user_action}' violates {self.name}")
        return False

if __name__ == "__main__":
    password_policy = SecurityPolicy("Password Policy", ["min 8 chars", "uppercase", "number"])
    acceptable_use = SecurityPolicy("Acceptable Use Policy", ["no torrent", "no unauthorized software"])

    password_policy.check_compliance("Password with min 8 chars and number")
    acceptable_use.check_compliance("Install unauthorized software")
