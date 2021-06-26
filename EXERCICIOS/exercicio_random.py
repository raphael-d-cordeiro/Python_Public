import random
import string

# int number generate between 10 and 20
# int_number = random.randint(10, 20)
# random int using the function range()
int_number = random.randrange(900, 1000, 10)

# float number generate between 10 and 20
# float_number = random.uniform(10, 20)

# float number generate between 0 and 1
float_number = random.random()

list_names = ['Raphael', 'Douglas', 'Felipe', 'Lucas', 'Jenny', 'Rose']
# one winner
# winner = random.choice(list_names)

# repeat name
# winner = random.choices(list_names, k=2)

# don't repeat name
winner = random.sample(list_names, k=2)

# shuffle list
random.shuffle(list_names)

# password generate
pass_letters = string.ascii_letters
pass_dig = string.digits
pass_char = '!@#$%¨&*()_+'

pass_combination = pass_letters + pass_dig + pass_char
password_user = "".join(random.choices(pass_combination, k=8))

print(password_user)
print(winner)
print(int_number)
print(float_number)
