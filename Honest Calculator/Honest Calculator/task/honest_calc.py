msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

symbols = ['+', '-', '*', '/']
memory = 0
msg_index = 10
a = 0

def is_one_digit(v):
    if float(v) > -10 and float(v) < 10 and float(v).is_integer():
        output = True
    else:
        output = False
    return output

def is_one_digit2(v):
    if float(v) > -10 and float(v) < 10 and float(v).is_integer():
        print(msg_10)
        answer = input()
        msg_index = 10
        while answer == 'y' and msg_index < 12:
            msg_index += 1
            if msg_index == 11:
                print(msg_11)
                answer = input()
            if msg_index == 12:
                print(msg_12)
                answer = input()
            else:
                break
        if answer == 'y' and msg_index == 13:
            return True
        else:
            return False




def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (float(v1) == 1 or float(v2) == 1) and v3 == '*':
        msg += msg_7
    if (float(v1) == 0 or float(v2) == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8

    if msg != '':
        msg = msg_9 + msg
        print(msg)

while True:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split()

    if x == 'M':
        x = memory
    elif y == 'M':
        y = memory

    try:
        a = float(y)
        b = float(x)
    except ValueError:
        print(msg_1)
        continue

    if oper not in symbols:
        print(msg_2)
        continue

    check(x, y, oper)

    y = float(y)
    x = float(x)

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/' and y != 0:
        result = x / y
    else:
        print(msg_3)
        continue

    print(result)


    while True:
        print(msg_4)
        answer = input()
        if answer == 'y' or answer == 'n':
            break
        else:
            continue

    if answer == 'y' and is_one_digit2(result):
            memory = result




    while True:
        print(msg_5)
        answer = input()
        if answer == 'y' or answer == 'n':
            break
        else:
            continue
    if answer == 'y':
        continue
    elif answer == 'n':
        break