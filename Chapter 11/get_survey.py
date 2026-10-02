from survey import AnonymousSurvey


question = "What type of burger you like to eat?"
liked_burger_survey = AnonymousSurvey(question)
liked_burger_survey.show_question()
while True:
    print("Enter q any time to end the program:")
    prompt = input("Type hear: ")
    if prompt == 'q' or prompt == 'Q':
        break
    liked_burger_survey.get_response(prompt)
liked_burger_survey.show_response()




