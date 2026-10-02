class AnonymousSurvey:
    
    def __init__(self, questions):
        self.question = questions
        self.response = []
    def show_question(self):
        print(self.question)
    def get_response(self, response):
        self.response.append(response)
    def show_response(self):
        print("Survey result: ")
        for responde in self.response:
            print("\t",responde)

        
        