import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
numbers=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

num_letters = int(input("How many letters? "))
num_symbols = int(input("How many symbols? "))
num_numbers = int(input("How many numbers? "))

lst_letters = num_letters*"l" #GENERATE RANDOM LETTERS!!!
lst_letters = list(lst_letters)
init_let = "" 

for l in lst_letters:
    l = random.choice(letters)
    init_let = init_let + l

init_let = list(init_let)

#___________________________________________________________________

lst_symbols = num_letters*"s" #GENERATE RANDOM SYMBOLS
lst_symbols = list(lst_symbols)
init_sym = ""

for s in lst_symbols:
    s = random.choice(symbols)
    init_sym = init_sym + s
init_sym = list(init_sym)

#___________________________________________________________________
lst_numbers = num_numbers*"n" #GENERATE RANDOM NUMBERS
lst_numbers = list(lst_numbers)
init_num = ""

for n in lst_numbers:
    n = random.choice(numbers)
    init_num = init_num + n
init_num = list(init_num)

#___________________________________________________________________
password = init_num+init_let+init_sym
password = random.sample(password, len(password))
str_password ="" 
password = str_password.join(password)
print(password)
