def check_encryption_strength(algorithm):
    print(f"🔐 Checking encryption algorithm: {algorithm}")
    quantum_vulnerable = ["RSA", "ECC", "DSA"]
    quantum_resistant = ["AES-256", "SHA-3", "Lattice-based", "Hash-based"]

    if algorithm in quantum_vulnerable:
        print("🚨 Vulnerable to quantum attacks (Shor’s Algorithm)")
    elif algorithm in quantum_resistant:
        print("✅ Resistant to quantum attacks (Post-Quantum safe)")
    else:
        print("ℹ️ Unknown algorithm → Further research needed")

if __name__ == "__main__":
    algorithms = ["RSA", "ECC", "AES-256", "SHA-3", "Lattice-based"]
    for algo in algorithms:
        check_encryption_strength(algo)
