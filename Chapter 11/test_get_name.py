import get_name as gn

def test_get_name():
    formatted_name = gn.get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
    
