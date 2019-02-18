def complement(num_of_complement, num_s_complement):
    if int(num_of_complement) == 10:
        result = (10 ** len(str(num_s_complement))) - int(num_s_complement)
        return result
    else:
        len_complement = len(num_s_complement)
        top_of_num = ""
        for i in range(0, len_complement):
            top_of_num += num_of_complement
        result = (int(top_of_num) - int(num_s_complement))
        return result


def decimal_to_binary(number):
    binary = ""
    div = 3
    while(div >= 2):
        div = number // 2
        remainder = number % 2
        number = div
        binary += str(remainder)
        if div < 2:
            binary += str(div)
    return binary[::-1]


def d_radix_complement(num):
    num_of_d_radix = ""
    for i in range(0, len(decimal_to_binary(num))):
        if decimal_to_binary(num)[i] == "0":
            num_of_d_radix += "1"
        else:
            num_of_d_radix += "0"
    return num_of_d_radix

def radix_complement(numb):
    decimal = 0
    #print("Uzunluk : {}".format(len(d_radix_complement(10))))
    for i in range(0, len(d_radix_complement(numb))):
        #print("Numara : {}".format(int(d_radix_complement(numb)[-(i+1)])))
        if int(d_radix_complement(numb)[-(i+1)]) == 0:
            pass
        else:
            print("2 ** i : {}".format(2**i))
            decimal += 2 ** i
        #print("i : {}\ndecimal {}: ".format(i, decimal))
    if len(decimal_to_binary(decimal + 1)) <= 3:
        return "0" + decimal_to_binary(decimal + 1)
    else:    
        return decimal_to_binary(decimal+1)

print("Decimal to binary -> {}\nDimenished radix complement -> {}\nRadix complement -> {}".format(decimal_to_binary(15), d_radix_complement(15), radix_complement(15)))