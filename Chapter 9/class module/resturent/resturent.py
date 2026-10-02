class Resturent:
    def __init__(self, resturent_name, cuisine_name):
        self.name = resturent_name
        self.cuisine = cuisine_name
        self.service = 10
    def describe_resturent(self):
        print(f"The {self.name.title()} is one of the famouse one in khanpur.")
        print(f"This resturent cuisine name is {self.cuisine.title()}\n")

    def resturent_open(self):
        print(f"Resturent ``{self.name.title()}`` is now open.")

    def number_surved(self, number=10):

        self.service = number
        print(f"This resturent served only {self.service} custmers\n")
    def increase_service(self, service):

        self.service += service
        print(f"{self.service} custmers are server in this buisness day.\n")
    

