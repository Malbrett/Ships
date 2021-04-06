import re
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
bigNum = 65537


class User:
    def __init__(self, userid):
        self.userid = userid

    @classmethod
    def new_user(cls, file):
        while True:
            new_name = input("Please enter a 4 character userID: ")
            new_name.lower()
            if re.match(r"\D\D\D\D", new_name):
                file.write(new_name+"\n")
                break
            else:
                print("That userID is invalid.")
        print("---")
        while True:
            new_pass = hashlib.sha256(input("Please enter a new secure password: ").encode()).hexdigest()
            print(new_pass)
            confirm_pass = hashlib.sha256(input("Please re-enter your secure password: ").encode()).hexdigest()
            print(confirm_pass)
            if new_pass == confirm_pass:
                file.write(str(new_pass)+"\n")
                break
            else:
                print("That password does not match.")
        print("---")
        private_key = rsa.generate_private_key(public_exponent=bigNum, key_size=2048)
        public_key = private_key.public_key()
        public_key = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                             format=serialization.PublicFormat.SubjectPublicKeyInfo)
        private_key = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PrivateFormat.PKCS8,
                                                encryption_algorithm=serialization.BestAvailableEncryption(b'new_pass'))

        # decode to printable strings
        private_key_str = private_key.decode('utf-8')
        public_key_str = public_key.decode('utf-8')

        prv = open(f"{new_name}_private.pem", "w")
        prv.write(private_key_str)
        #print('Private key = ')
        #print(private_key_str)
        prv.close()

        pub = open(f"{new_name}.pem", "w")
        pub.write(public_key_str)
        #print('Public key = ')
        #print(public_key_str)
        pub.close()


firstTime = False
try:
    open("userInfo", "x")
    user = open("userInfo", "a")
    firstTime = True
except FileExistsError:
    user = open("userInfo")
finally:
    if firstTime:
        user = open("userInfo", "a")
        User.new_user(user)
        user = open('userInfo')

username = user.readline(1)
print(f"Welcome {username}")
