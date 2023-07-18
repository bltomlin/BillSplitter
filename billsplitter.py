"""
This module contains all program logic that will be used
in this program.
"""
import random

empty_dict = {}

"""
User to input friends into dictionary.
"""
print("Enter the number of friends joining (including you):")
quantity = int(input())

if quantity <= 0:
    print("No one is joining for the party")

else:
    print("Enter the name of every friend (including you), each on a new line:")
    for x in range(int(quantity)):
        name = input()
        another_dict = {name:0}
        empty_dict.update(another_dict)


    """
    User to input bill total. The program calculates what everyone must pay.
    """  
    print("Enter the total bill value:")
    value = int(input())
    avg = round((value / quantity), 2)
    for names in empty_dict:
        another_dict = {names:avg}
        empty_dict.update(another_dict)


    """
    If user chooses, a random friend won't pay the bill and program will recalculate what everyone else must pay.
    """
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    ans = input()

  
    if ans == "Yes":
        key = random.choice(list(empty_dict.keys()))
        print(key)
        avg = round((value / (quantity - 1)), 2)
        for names in empty_dict:
            another_dict = {names:avg}
            empty_dict.update(another_dict)
        another_dict = {key:0}
        empty_dict.update(another_dict)
        print(empty_dict)
        
    else:
        print("No one is going to be lucky")
        print(empty_dict)
