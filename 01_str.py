# len בודקת כמה אותיות יש בביטוי
name = "danny"
print(f'lenght of danny is {len(name)}')

# upper lower הופך לאותיות גדולות / קטנות
print(str.upper(name))
friend = 'YOSSI'
print(str.lower(friend))

#switch between text old to new
x = "hello world"
print(x.replace("world", "danny"))

# make list of words with specific seperator להפוך מחרוזת לרשימה
sentence = "hello world good morning"
print(sentence.split())

# remove spaces from start + end להוריד רווחים מיותרים מההתחלה ומסוף
y = "     hello world good morning"
print(y.strip())

# upper to lower , lower to upper הופך את האותיות מגדול לקטן או הפוך
print(f'AhnjdnEjnnI'.swapcase())

#startswhit endswith
print(sentence.startswith("hello")) #true
print(sentence.endswith("world")) #false

# make the first letter upper case, all other lower case רק האות הראשונה במשפט
print(sentence.capitalize())

# each new word starts with upper case, all other lower case כל האותיות הראשוונות בכל מילה
print(sentence.title())

# isalpha checks if the str is only letters
print(name.isalpha()) #true

# isdigit checks if the str is only numbers
print(sentence.isdigit()) #false