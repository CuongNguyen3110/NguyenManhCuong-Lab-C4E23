from random import *
from calc_func import eval

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    y = randint(0,10)
    error = choice([-2,-1,0,0,0,1,2])
    op_list = ["+", "-", "*", "/"]
    op = choice(op_list)
    r = eval(x, y, op) + error
    return [x, y, op, r]

def check_answer(x, y, op, result, user_choice):
    if user_choice == True:
        if result == eval(x, y, op):
            return True
        else:
            return False
    if user_choice == False:
        if result != eval(x, y, op):
            return True
        else:
            return False
