import random
import string
import json
import os
from datetime import datetime

HISTORY_FILE = "password_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        print("Error: At least one character type must be selected!")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    score = 0
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    if score <= 2:
        return "WEAK", "red"
    elif score <= 4:
        return "MODERATE", "yellow"
    elif score <= 5:
        return "STRONG", "green"
    else:
        return "VERY STRONG", "bright_green"

def display_password_analysis(password):
    print("\n--- Password Analysis ---")
    print(f"Length: {len(password)} characters")
    print(f"Uppercase: {sum(1 for c in password if c.isupper())}")
    print(f"Lowercase: {sum(1 for c in password if c.islower())}")
    print(f"Digits: {sum(1 for c in password if c.isdigit())}")
    print(f"Special: {sum(1 for c in password if c in string.punctuation)}")
    strength, _ = check_password_strength(password)
    print(f"Strength: {strength}")

def generate_custom_password():
    print("\n--- Custom Password Generator ---")
    
    while True:
        try:
            length = int(input("Enter password length (4-64): "))
            if 4 <= length <= 64:
                break
            print("Please enter a number between 4 and 64.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    print("\nSelect character types (y/n):")
    use_uppercase = input("Include uppercase letters (A-Z)? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters (a-z)? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits (0-9)? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters (!@#$...)? (y/n): ").strip().lower() == 'y'
    
    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        print("At least one character type must be selected!")
        return None
    
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    return password

def generate_quick_password():
    print("\n--- Quick Password Generator ---")
    print("1. Weak (6 chars, letters only)")
    print("2. Moderate (8 chars, letters + digits)")
    print("3. Strong (12 chars, all types)")
    print("4. Very Strong (16 chars, all types)")
    
    choice = input("\nSelect strength (1-4): ").strip()
    
    if choice == '1':
        return generate_password(6, True, True, False, False)
    elif choice == '2':
        return generate_password(8, True, True, True, False)
    elif choice == '3':
        return generate_password(12, True, True, True, True)
    elif choice == '4':
        return generate_password(16, True, True, True, True)
    else:
        print("Invalid choice!")
        return None

def generate_batch():
    print("\n--- Batch Password Generator ---")
    
    while True:
        try:
            count = int(input("How many passwords to generate? (1-20): "))
            if 1 <= count <= 20:
                break
            print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    while True:
        try:
            length = int(input("Password length (4-64): "))
            if 4 <= length <= 64:
                break
            print("Please enter a number between 4 and 64.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    passwords = []
    for i in range(count):
        password = generate_password(length, True, True, True, True)
        passwords.append(password)
        print(f"{i+1}. {password}")
    
    return passwords

def view_history():
    history = load_history()
    if not history:
        print("\nNo password history found.")
        return
    
    print("\n--- Password History ---")
    print(f"{'#':<5} {'Date':<20} {'Length':<10} {'Password':<25}")
    print("="*60)
    for i, entry in enumerate(history[-10:], 1):
        print(f"{i:<5} {entry['date']:<20} {entry['length']:<10} {entry['password']:<25}")
    print("="*60)

def clear_history():
    confirm = input("Clear all password history? (y/n): ").strip().lower()
    if confirm == 'y':
        save_history([])
        print("History cleared!")
    else:
        print("Cancelled.")

def main():
    history = load_history()
    
    print("="*50)
    print("     PASSWORD GENERATOR")
    print("="*50)
    
    while True:
        print("\n===== PASSWORD GENERATOR =====")
        print("1. Custom Password")
        print("2. Quick Password")
        print("3. Batch Generate")
        print("4. View History")
        print("5. Clear History")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            password = generate_custom_password()
            if password:
                print(f"\nGenerated Password: {password}")
                display_password_analysis(password)
                history.append({
                    'password': password,
                    'length': len(password),
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                save_history(history)
        
        elif choice == '2':
            password = generate_quick_password()
            if password:
                print(f"\nGenerated Password: {password}")
                display_password_analysis(password)
                history.append({
                    'password': password,
                    'length': len(password),
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                save_history(history)
        
        elif choice == '3':
            passwords = generate_batch()
            for pw in passwords:
                history.append({
                    'password': pw,
                    'length': len(pw),
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            save_history(history)
        
        elif choice == '4':
            view_history()
        
        elif choice == '5':
            clear_history()
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
