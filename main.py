import hashlib
bigNum = 104729


class User:
    def __init__(self, userid):
        self.userid = userid

    @classmethod
    def newUser(cls, file):
        while True:
            newname = input("Please enter a 4 character userID: ")
            newname.lower()
            if len(newname) == 4:
                file.write(newname)
                break
            else:
                print("That userID is not 4 characters.")
        print("---")
        while True:
            newpass = hashlib.sha256(input("Please enter a new secure password: ").encode()).hexdigest()
            print(newpass)
            confirmpass = hashlib.sha256(input("Please re-enter your secure password: ").encode()).hexdigest()
            print(confirmpass)
            if newpass == confirmpass:
                file.write(str(newpass))
                break
            else:
                print("That password does not match.")
        print("---")



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
        User.newUser(user)

username = user.readline(1)
print(f"Welcome {username}")
