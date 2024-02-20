import re
common_word= ['admin', '12345', 'password']

def pessword_strong(password):
          if len(password) < 8:
               return False
     
          if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"/d", password) or not re.search(r"[!@#$%^&*()-_=+[{]}\|;:',<.>/?]", password):
           return False
     
    
          for word in common_words:
               if word in password.lower():
                    return False

                    return True

def main():
     password= input("הזן סיסמה: ")
if is_password_strong(password):
        print("הסיסמא חזקה")
else:
        print("הסיסמא אינה חזקה")
           
if __name__ == "__main__":
    main()

   