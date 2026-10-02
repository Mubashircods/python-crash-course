from survey import AnonymousSurvey as a 

def test_AnonymousSurvey_class():
    question = "Which type of food you want to eat: "
    liked_food = a(question)
    liked_food.get_response("Mutton")
    assert "Mutton" in liked_food.response