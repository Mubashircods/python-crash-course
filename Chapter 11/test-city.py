from problems import city_country


def test_city_country():
    formate_pair = city_country("karachi", "pakistan")
    assert formate_pair == "Karachi: Pakistan"