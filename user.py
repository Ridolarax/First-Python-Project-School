# from login import login1
# import register



class User:
    """This Class welcomes the user to the main page, then
        Asks the iser if he's a new user or existing
        if new:
            calls to register()
        else:
            calls to login()
    """

    def __init__(self) -> None:
        pass

    def welcome_user(self):
        """This Prompts the user Immediately to the home page
            And further the  Questions
        """

        self.user_opinion = input("Log in  ||  Register ? (Type L to Login and R to Register as a new user!): \n").title()
        if self.user_opinion == "R":
            print("Yes")
            from register import register1
        elif self.user_opinion == "L":
            print("NO man!!!!!")
            from login import login1
        else:
            print("Are you blind, mfk?!! ".upper())


user1 = User()
user1.welcome_user()