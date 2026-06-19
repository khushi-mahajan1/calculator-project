import string
import random
def generate_password(length,use_upper,use_lower,use_digits,use_symbols):
    characters=""
    if use_upper:
        characters+=string.ascii_uppercase
    if use_lower:
        characters+=string.ascii_lowercase
    if use_digits:
        characters+=string.digits
    if use_symbols:
        characters+=string.punctuation
        
    if not characters:
        return None
    password=""
    for _ in range(length):
        password+=random.choice(characters)
    return password
def main():
    print("=" * 50)
    print("       Professional Password Generator")
    print("=" * 50)
    try:
        length=int(input("Enter the length of the Password:"))
        if length<4:
            print("The length of the password should be atleast 4..")
            return
        use_upper=input("Include uppercase letters (yes/no) ?:").lower()=="y"
        use_lower=input("Include Lowercase letters (yes/no) ? :").lower()=="y"
        use_digits=input("Include Digit in the password (yes/no) ? :").lower()=="y"
        use_symbols=input("Include the special characters (yes/no) ?:").lower()=="y"
        password=generate_password(length,use_upper,use_lower,use_digits,use_symbols)
        if password:
            print("\nGenerated Password:")
            print(password)
        else:
            print("Please select at least one charater type:")
    except ValueError:
        print("Please Enter the Valid Number...")
if __name__=="__main__":
    main()
        