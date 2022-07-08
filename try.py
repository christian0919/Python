from os import lseek
from warnings import catch_warnings

num=0
total=0.0
while True :
    
    value = input('Enter a number: ')
    if value == 'end' :
        break
    try :
        valueFloat = float(value)
    except :
        print("Error: Invalid input");
        continue
    num = num+1
    total = valueFloat + total

print("total:", total)
