def persistence_simulation(method):
    print(f"🔒 Simulating persistence via: {method}")
    if method == "registry run key":
        print("   Action: Add entry to Windows registry → Run at startup (simulation only)")
    elif method == "scheduled task":
        print("   Action: Create hidden scheduled task → Execute payload daily (simulation only)")
    elif method == "dll injection":
        print("   Action: Inject malicious DLL into legitimate process (simulation only)")
    elif method == "web shell":
        print("   Action: Deploy web shell → Remote access via HTTP (simulation only)")
    else:
        print("   No persistence simulation available")

if __name__ == "__main__":
    methods = ["registry run key", "scheduled task", "dll injection", "web shell"]
    for m in methods:
        persistence_simulation(m)
