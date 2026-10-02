from user import Users
class Privileges:

    def __init__(self, privilages=['can add post', 'can delete post', 'can ban user',]):
        self.privilages = privilages

    def show_privileges(self):
        print(f"Admin privileges:")
        for privilege in self.privilages:
            print(f"\t {privilege}.")


class Admin(Users):
    def __init__(self, first_name, last_name, age='', location=''):
        super().__init__(first_name, last_name, age, location)
        self.privileges_string = Privileges()
    