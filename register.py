class Register:
    """ Get users info, then calls in the users_info.txt to check if the user is registered;
        if registered before:
            Redirect the user to the login.py;
        ELSE:
            Registers the user and direct him to the login.py
    """

    file_name = "user_info.txt"

    def __init__(self) -> None:
        # constructor automatically calls to the prompt_user_info()
        
        self.prompt_user_info()
        
    def prompt_user_info(self):
        """Asks the user for their username and password, and also give chance to verify the password
            Then, automatically calls in the check_user_account()
        """
        self.username = input("Input username: ")
        self.password = input("Input your password: ")
        self.verify_password = input("Verify your password: ")
        
        self.check_user_account()

    def check_user_account(self):
        """ Checks for the occurence of the user in the user_info.txt file,
            If input username is present, prompt the user to give other input, ELSE:
            it registers the user in the user_info.txt file
        """

        with open(Register.file_name, "r") as f:
            file_content = f.read()

            if self.username in file_content:
                print("This username exists, try another!") # if username is present in the file, Don't Register!
                self.prompt_user_info() # Calls to start from the beginning again.......
            else:
                # if username is new, Register it.... but
                # verify password first, then  call to register().......
                
                if self.verify_password == self.password:    
                    self.register()
                    print(f"Thanks for Signing Up mr {self.username}")
                    opinion = input("Will you like to Log in now? ")
                    
                    if opinion == "Yes":
                        print("Okay")
                    else:
                        print("Are you mad? ")
                else:
                    print("Verify your password!!! ")
                    self.prompt_user_info()

    def register(self):
        with open(Register.file_name, "a") as f:
            user_info = self.username + "\t" + self.password
            f.write(user_info + "\n")


register1 = Register()
