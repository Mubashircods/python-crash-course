from pathlib import Path


def test_write_note():
    while True:
        path_title = input("Enter your title: ")
        root = Path(path_title + ".txt")
        prompt = input("Write your notes: ")
        while True:
            ask_new_line = input("Want to add new line (yes/no): ")
            if ask_new_line == 'yes':
                new_line = input("Write your note: ")
                prompt += f"\n{new_line}"
            else:
                break
        root.write_text(prompt)
        
        new_notes = input("Want to write new note (yes/no): ")
        if new_notes == 'no':
            print('Note save successful.')
            break


test_write_note()


