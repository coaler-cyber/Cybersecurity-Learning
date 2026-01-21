def smart_contract_check(contract):
    print(f"📜 Smart Contract Security Report for: {contract['name']}")
    
    if contract.get("reentrancy_vulnerable"):
        print("🚨 Reentrancy vulnerability detected")
    else:
        print("✅ No reentrancy issue")
    
    if contract.get("integer_overflow"):
        print("🚨 Integer overflow vulnerability detected")
    else:
        print("✅ No integer overflow issue")
    
    if not contract.get("access_control"):
        print("🚨 Missing access control → High risk")
    else:
        print("✅ Access control implemented")

if __name__ == "__main__":
    contract_example = {
        "name": "TokenContract",
        "reentrancy_vulnerable": True,
        "integer_overflow": False,
        "access_control": True
    }
    smart_contract_check(contract_example)
