def vulnerable_service(input_data):
    if len(input_data) > 10:
        raise Exception("🚨 Zero-Day triggered: Buffer overflow!")
    return "✅ Service executed successfully"

def zero_day_exploit():
    print("🎯 Running Zero-Day Exploit Simulation...")
    payload = "A" * 20
    try:
        result = vulnerable_service(payload)
        print(result)
    except Exception as e:
        print(f"Exploit successful → {e}")

if __name__ == "__main__":
    zero_day_exploit()
