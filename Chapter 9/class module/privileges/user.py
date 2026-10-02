class Users:
    def __init__(self, first_name, last_name, age='', location=''):
        self.first_name = first_name
        self.last_name = last_name
        self.login_atempt = 0
        self.age = age
        self.location = location

    def discribe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        if self.location and self.age:
            print(f"The full name of user is {full_name.title()}\n"
                  f"Their age is {self.age}\nAnd their location is {self.location}")
        elif self.age:
            print(f"The full name of user is {full_name.title()}\n"
                  f"Their age is {self.age}")
        else:
            print(f"The full name of user is {full_name.title()}")

    def greet_user(self):
        full_name = self.first_name +' '+self.last_name
        print(f"Hello {full_name.title()}! Thank you to come in my site.\n")
    
    def increase_login_attempt(self, attempt=1):
        self.login_atempt += attempt

    def reset_login_attempt(self):
        self.login_atempt = 0






