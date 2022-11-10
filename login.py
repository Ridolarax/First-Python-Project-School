from takeaCourse import TakeaCourse
from takeaCourse import TakeaCourse
import json

class Login:
    file_name = "user_info.txt"
    """Prompts the User to input their username and password,
       Calls in the user_info.txt file to check for thier occurrence,
       If both are found:
        proceed to TakeaCourse
       Else:
        proceed to Register
    """
    
    def __init__(self) -> None:
        """AUTOMATIC CALL TO ask_user_info()
        """
        self.ask_user_info()

    def ask_user_info(self):
        """Prompts the User for the Username and password
        """
        self.username = input("Input your username: ")
        self.password = input("Input your password: ")

    def check_user_account(self):
        """Calls in the user_info.txt file and check the input against the file.
           If found:
                Login and proceed to take the course
            Else:
                Proceed to Register
        """

        with open(Login.file_name, "r") as fp:
            username_list = []
            password_list = []

            for lines in fp:
                username, password = lines.split()
                username = username.strip()
                password = password.strip()

                username_list.append(username)
                password_list.append(password)

            data = dict(zip(username_list, password_list))
            # print(data)

            if self.username in data:
                if self.password == data[self.username]:  # if username is found in the data, call to the taketheCourse()
                    print("Yes")
                    file_name = "user_info.json"
                    with open(file_name, "w") as fp:
                        json.dump(self.username, fp)
                    TakeaCourse()
                else:
                    print("wrong password")
            else:
                print("Probably You've not Registered before")
                # call to register() to register the new user.


login1 = Login()
# login1.ask_user_info()
login1.check_user_account()
