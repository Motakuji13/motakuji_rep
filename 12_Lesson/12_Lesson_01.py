x = int (input())
y = int (input ())

try:
    res = x / y
except ZeroDivisionError:
    print ("Вы ввели 0")
    res = 0
print (res)




name = input("")    