import random
import time


MAXLINES = 3
MAXBET = 10000
MINBET = 10

ROWS = 3
COLS = 3

symbol_count = {"A":4,"B":8,"C":10,"D":18}

symbol_value = {"A":5,"B":4,"C":3,"D":2}

def check_win(columns,lines,bet,values):
    winnings = 0
    win_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            win_line.append(line + 1)
    
    return winnings,win_line



def getspin(rows,cols,symbols):
    all_symbols=[]

    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def printmachine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end = " | ")
            else:
                print(column[row],end = " | ")
        print()



def deposit():
    while True:
        amount = input("What would you like to deposite? : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount should be more than zero!")
        else:
            print("Please enter a numbeer")
    return amount

def number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on(1 to "+ str(MAXLINES)+") : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXLINES :
                break
            else:
                print("Enter valid number of lines!")
        else:
            print("Please enter a numbeer")
    return lines

def getbet():
    while True:
        amount = input("What would you like to bet on each line? : ")
        if amount.isdigit():
            amount = int(amount)
            if MINBET <= amount <= MAXBET:
                break
            else:
                print(f"amount should be between {MINBET} - {MAXBET}! ")
        else:
            print("Please enter a numbeer")
    return amount


def spin(balance):
    lines = number_of_lines()
    while True:

        bet = getbet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f'you do not have enough monet to bet!,current balance is: {balance}')
        else:
            break
    print(f"You are betting {bet} on {lines} lines.")
    time.sleep(1)
    print(f'total bet is : {total_bet}')
    time.sleep(1)
    slots = getspin(ROWS,COLS,symbol_count)
    printmachine(slots)
    winnings, win_line = check_win(slots,lines,bet,symbol_value)
    print(f"You won: {winnings}!")
    time.sleep(1)
    print(f"You won on line : ",*win_line)
    time.sleep(1)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is : {balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer== "q":
            break
        balance += spin(balance)

    print(f"You left with : {balance}")


main()
