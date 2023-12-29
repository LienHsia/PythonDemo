
import random

numbers = list(range(1, 9)) * 2
random.shuffle(numbers)

def display_board():
    for i in range(0, 16, 4):
        print(numbers[i:i+4])

def remove_numbers(x1, y1, x2, y2):
    global numbers
    numbers[x1*4+y1] = 0
    numbers[x2*4+y2] = 0

def is_valid_move(x1, y1, x2, y2):
    if x1 == x2 and abs(y1-y2) == 1:
        return True
    if y1 == y2 and abs(x1-x2) == 1:
        return True
    return False

display_board()
while True:
    x1 = int(input('请输入第一个数字的行号（0-3）：'))
    y1 = int(input('请输入第一个数字的列号（0-3）：'))
    x2 = int(input('请输入第二个数字的行号（0-3）：'))
    y2 = int(input('请输入第二个数字的列号（0-3）：'))
    if is_valid_move(x1, y1, x2, y2) and numbers[x1*4+y1] == numbers[x2*4+y2]:
        remove_numbers(x1, y1, x2, y2)
        display_board()
        if all(num == 0 for num in numbers):
            print('恭喜你，游戏结束！')
            break
    else:
        print('无效的移动，请重新输入。')