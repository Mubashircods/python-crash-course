from pathlib import Path


try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide intigers by zero.')



print("\nYou give me two number and then i'll divide these numbers.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print("\n",answer)




def count_words(path):
    """Count the approximate number of words in files."""
    try:
        
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_lenth = len(words)
        print(f"\nThis {path} file has about {num_lenth} words.")

path1 = Path('alice.txt')
count_words(path1)


folder_files = ['alice.txt', 'sidhartha.txt', 'learn_python.txt']
for folder_file in folder_files:
    path2 =  Path(folder_file)
    count_words(path2)



