# Solution 10.1
from pathlib import Path


# learn = Path('learn_python.txt')
# contents = learn.read_text()
# print(contents)

# line_list = ''
# for content in contents:
#     line_list += content
# print("\n",line_list)




# # Solution 10.2 continued to 10.1

# print(f"\n{line_list.replace('Python', 'C')}")




# # Solution 10.3

# """This problem tell to remove temporary variable lines
# and use direct content.splitlines() methon in filework.py"""
# # Problem is solved.




# # Solution 10.4
# guess = input("Enter your name: ")
# write = Path('guess.txt')
# write.write_text(guess.title())




# # Solution 10.5
# names = ''
# while True:
#     guess_name = input("\n(Enter 'q' to close the program.)\nEnter your name: ")
#     if guess_name == 'q':
#         break
#     names += f"{guess_name}\n"

# name = Path('guess_book.txt')
# name.write_text(names.title())




# # Solution 10.6
# print('\nYou give me two number and then i add them.')


# first_number = input("\nFirst number: ")

# second_number = input("Second number: ")
# try:
#     result = int(first_number) + int(second_number)
# except ValueError:
#     print("Sorry, Invalid input.")
# else:
#     print(result)




# # Solution 10.7
# print("Enter two numbers and then i add these numbers.")
# print("Enter 'q' to quit.")
# while True:
#     first_num = input("First number: ")
#     if first_num == 'q':
#         break
#     second_num = input("Second number: ")
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num) + int(second_num)
#     except ValueError:
#         print("Sorry, Invalid input.")
#     else:
#         print(answer)




# # Solution 10.8
# cat = Path('cat.txt')
# dog = Path('dog.txt')

# try:
#     content = cat.read_text()
    
# except FileNotFoundError:
#     print(f"Sorry, no {cat} file exist.")
# else:
#     print(content)
# try:
#     con = dog.read_text()
# except FileNotFoundError:
#      print(f"Sorry, no {dog} file exist.")
# else:
#     print(con)




# # Solution 10.9
# cat = Path('cat.txt')
# dog = Path('dog.txt')

# try:
#     content = cat.read_text()
    
# except FileNotFoundError:
#     pass
# else:
#     print(content)
# try:
#     con = dog.read_text()
# except FileNotFoundError:
#      pass
# else:
#     print(con)




# Solution 10.10
patH = Path('alice.txt')

read_file = patH.read_text(encoding='utf-8')
count_word = read_file.count('alice ')
count_word_lower = read_file.lower().count('alice')
count_another_word = read_file.lower().count('the ')


print(f"Word 'the' is about {count_word} time occure in file {patH}")
print(f"Word 'the' is about {count_word_lower} time occure in file {patH}")
print(f"Word 'the' is about {count_another_word} time occure in file {patH}")


# Solution 10.11
# This problem is solved in folder Json data problems.




