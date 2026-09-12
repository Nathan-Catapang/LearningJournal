import math
import random
import time

def main():
    print("====================================")
    print("📡 DEEP-SPACE TARGET TRACKER INITIALIZED")
    print("====================================\n")
    print("A rogue asteroid is heading toward your sector.")
    print("Calculate the correct interception angle to destroy it.\n")
    
    # Generate random target coordinates
    target_x = random.randint(10, 50)
    target_y = random.randint(10, 50)
    
    # Calculate the exact mathematical angle needed
    # angle = arctan(y / x) converted to degrees
    exact_angle = math.degrees(math.atan2(target_y, target_x))
    
    print(f"🛰️  Target Telemetry:")
    print(f"   -> Distance X-axis: {target_x} light-years")
    print(f"   -> Distance Y-axis: {target_y} light-years")
    print("------------------------------------")
    
    attempts = 3
    while attempts > 0:
        try:
            guess = float(input(f"⚠️ Enter firing angle in degrees (0-90) [{attempts} attempts left]: "))
        except ValueError:
            print("❌ Invalid input. Enter a number.")
            continue
            
        # Check precision within 1.5 degrees of tolerance
        if math.isclose(guess, exact_angle, abs_tol=1.5):
            print("\n💥 DIRECT HIT! The asteroid has been neutralized.")
            print(f"Target locked exactly at {exact_angle:.2f}°.")
            return
        elif guess < exact_angle:
            print("📉 Too low! Aim higher.")
        else:
            print("📈 Too high! Aim lower.")
            
        attempts -= 1
        print("------------------------------------")
        
    print(f"\n🛸 MISSION FAILED. The asteroid slipped past.")
    print(f"The correct firing angle was: {exact_angle:.2f}°")

if __name__ == "__main__":
    main()
