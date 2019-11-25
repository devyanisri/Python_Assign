
j=6   
str=input("Enter String")
printString = ''
for i in str:
    printString = printString + i
    print(" "*j + printString)
    j-=1