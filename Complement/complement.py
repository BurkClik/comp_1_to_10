def complement(num_of_complement, num_s_complement):
    """num_s_complenet, num_of_complement'e complementi"""
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
    """This function is converting decimal number to binary."""
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


def binary_to_decimal(number):
    decimal = 0
    for i in range(0, len(number)):
        decimal += int(number[-(i + 1)]) * (2 ** i)
    return decimal


def d_radix_complement(num):
    num_of_d_radix = ""
    for i in range(0, len(decimal_to_binary(num))):
        if decimal_to_binary(num)[i] == "0":
            num_of_d_radix += "1"
        else:
            num_of_d_radix += "0"
    return num_of_d_radix


def radix_complement(numb):
    temp = decimal_to_binary(binary_to_decimal(d_radix_complement(numb)) + 1)
    if len(decimal_to_binary(binary_to_decimal(d_radix_complement(numb)) + 1)) <= 3:
        while(len(temp) <= 3):
            temp = "0" + \
                decimal_to_binary(binary_to_decimal(
                    d_radix_complement(numb)) + 1)
            temp_result = temp
            temp = "0" + temp_result
        return temp
    else:
        return decimal_to_binary(binary_to_decimal(d_radix_complement(numb)) + 1)


def addition(*args):
    pass


""" print(complement("9", "27"))
print(decimal_to_binary(11))
print(binary_to_decimal("1011"))
print(d_radix_complement(11))
print(radix_complement(11)) """
