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
                file.write(newname+"/n")
                break
            else:
                print("That userID is not 4 characters./n")
        print("---")
        while True:
            newpass = hashlib.sha512(input("Please enter a new secure password: "))
            confirmpass = hashlib.sha512(input("Please re-enter your secure password: "))
            if newpass == confirmpass:
                file.write(str(newpass)+"/n")
                break
            else:
                print("That password does not match./n")
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
