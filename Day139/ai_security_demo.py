import numpy as np

def simple_model(x):
    return "Positive" if x > 0.5 else "Negative"

def adversarial_attack(x):
    noise = np.random.uniform(-0.1, 0.1)
    adv_x = x + noise
    print(f"Original input: {x}, Adversarial input: {adv_x}")
    print(f"Model prediction (original): {simple_model(x)}")
    print(f"Model prediction (adversarial): {simple_model(adv_x)}")

if __name__ == "__main__":
    adversarial_attack(0.55)
    adversarial_attack(0.45)
