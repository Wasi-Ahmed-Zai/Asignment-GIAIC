import random as rd
import string

def password_generate(lenght):
    characther = string.ascii_letters + string.digits + string.punctuation
    password = "".join(rd.choice(characther) for _ in range(lenght))
    return password

    
lenght = int(input("Enter the desirec password lenght: "))


if __name__ == "__main__":
   password =  password_generate(lenght)
   print(f"Generated Password: {password}")
