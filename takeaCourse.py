import json

class TakeaCourse:
    """Lets the confirmed user take a course.
        But first, it gets user's info from the Login program and greet the user
        Asks the user whether to take a course or stop the program
        if TakeaCourse:
            Ask course_code
                if course_code:
                    open the file and read
                else:
                    tells the user the course_code is unknown
    """

    def __init__(self) -> None:
        self.greet_user()

    def greet_user(self):
        file_name = "user_info.json"
        with open(file_name, "r") as fp:
            username = json.load(fp)

        print(f"Welcome Oh {username}")
        self.select_course()

    def select_course(self):
        """Prompts the User to input the course they will like to Take:
        """
        course_name = input("What course will you like to take ? (Input course Title): ")



