

'''
1
name = "Danny"
# Fix this line:
print(f"{name} your name is in length len(name)")

2
first_name = "Petros"
last_name = "Borchardt"
id_num = "63 251283 B 185"
phone = "0419-0288803"

# Expected Output Layout: (use center)
# | Borchardt, Petros     |
# | ID: [63 251283 B 185] |
# | Phone: 0419-0288803   |

3
Given the dirty input string user_input = "   jOhN_dOe_2026   ",
write python expressions to:Remove the leading and trailing whitespaces
Convert the entire string to lowercase
Replace all underscores (_) with hyphens (-)

4
answer True/False
print("python3".isalpha())
print("12 34".isdigit())
print("   ".isspace())
print("HELLO".isupper())
print("hi".islower())

5
msg = "step on no pets"
check if we reverse this str we get the same string

6
Given the string course = "Python Core Study Mechanics"
check if the first word "Python"
check if the last word "Mechanics"
split this sentence into a string of words and print it
'''

#1
name = 'Danny'
print(f"{name} your name is in length {len(name)}")

#2
first_name = "Petros"
last_name = "Borchardt"
id_num = "63 251283 B 185"
phone = "0419-0288803"
full_name = f'{first_name} {last_name}'
print('|', full_name.center(21),'|')
print('|',id_num.center(21),'|')
print('|',phone.center(21),'|')






#3
user_input = "   jOhN_dOe_2026   "
print(user_input.strip())
print(user_input.lower())
print(user_input.replace("_", "-"))
print(user_input.strip().replace(" ", "-").lower())

#4
#false
#false
#true
#true
#true

#5
msg = "step on no pets"
print("revers",msg == msg[::-1])

#6
course = "Python Core Study Mechanics"
print(course.startswith("Python"))
print(course.endswith("Mechanics"))
print(course.split(" "))



#7
#"Python Core Study Machanics"
# run on this string , print each charcter in a new line using a for loop
# dont print space

python = "Python Core Study Machanics"
for char in python:
    if not char.isspace():
        print(char)


