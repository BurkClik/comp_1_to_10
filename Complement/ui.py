# coding=utf-8
import complement as comp

s = """1 - Compelement
2 - Decimal to binary
3 - Binary to decimal
4 - D-Radix complement
5 - Radix Complement\n"""

flag = True

print(s)

while flag != False:
    islem = int(input("Numara gir : "))
    if (islem != 0):
        if (islem == 1):
            num_of_complement = str(input("num_of_complement : "))
            num_s_complement = str(input("num_s_complement : "))
            print(comp.complement(num_of_complement, num_s_complement)+"\n")
        elif (islem == 2):
            number = int(input("Number : "))
            print(comp.decimal_to_binary(number)+"\n")
        elif (islem == 3):
            number = str(input("Number : "))
            print(comp.binary_to_decimal(number)+"\n")
        elif (islem == 4):
            num = int(input("Number : "))
            print(comp.d_radix_complement(num)+"\n")
        elif (islem == 5):
            numb = int(input("Number : "))
            print(comp.radix_complement(numb)+"\n")
        elif (islem == 0):
            flag = False
        else:
            islem = int(input("Numara gir : "))
            print(s+"\n")
        print(s)
    else:
        flag = False
