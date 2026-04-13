from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class HRD_024:
    def __init__(self,password : str):
        self.password = password
    
    def genrateKey(self):
        salt = b"Prajapati__Hardik__24" # this is my salt 
        kdf= PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            salt=salt,
            length=32,
            iterations=100000# 100000 times loop will Hash the password 
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        return key

    def encryptMessage(self,message):
        self.message = message
        key = self.genrateKey()
        f = Fernet(key)
        Encrypted_message = f.encrypt(message.encode()).decode()
        return Encrypted_message

    def decryptMessage(self,message):
        try:
            self.message = message
            key = self.genrateKey()
            f = Fernet(key)
            Decrypted_Message = f.decrypt(self.message)
            return Decrypted_Message
        except:
            return "Wrong Password ! "
def main():
    print("-" * 30)
    print("🚀 GHOST CIPHER V1.0")
    print("👤 Dev: HRD-024")
    print("-" * 30)

    passwo = input("[*] Enter Master Password to start: ")
    agent = HRD_024(passwo)

    while True:
        print("\n--- MENU ---")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Change Password")
        print("4. Exit")
        
        choice = input("\n[?] Select Option (1-4): ")

        if choice == '1':
            msg = input("\nEnter message to encrypt: ")
            print(f"\n[+] Encrypted: {agent.encryptMessage(msg)}")
        
        elif choice == '2':
            msg = input("\nEnter encrypted text: ")
            print(f"\n[+] Decrypted: {agent.decryptMessage(msg)}")
        
        elif choice == '3':
            new_pass = input("\nEnter new Master Password: ")
            agent.password = new_pass
            print("[✓] Password updated!")

        elif choice == '4':
            print("\nShutting down Ghost Cipher... Goodnight Agent HRD-024! 😼")
            break
        
        else:
            print("[!] Invalid Choice!")

if __name__ == "__main__":
    main()