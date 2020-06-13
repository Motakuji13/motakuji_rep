with open('D:\\Programming\\01_Python\\motakuji_rep\\14_Lesson\\test.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input())
    line = str('1 / ' + str(num) + ' = ' + str(1 / num))
    print(line)
    inFile.write (line)
    
name = input("")