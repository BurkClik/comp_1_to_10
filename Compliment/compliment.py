def compliment(num_of_compliment, num_s_compliment):
    if int(num_of_compliment) == 10:
        result = (10 ** len(str(num_s_compliment))) - int(num_s_compliment)
        return result
    else:
        len_compliment = len(num_s_compliment)
        top_of_num = ""
        for i in range(0, len_compliment):
            top_of_num += num_of_compliment
        result = (int(top_of_num) - int(num_s_compliment))
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


def d_radix_compliment(num):
    num_of_d_radix = ""
    for i in range(0, len(decimal_to_binary(num))):
        if decimal_to_binary(num)[i] == "0":
            num_of_d_radix += "1"
        else:
            num_of_d_radix += "0"
    return num_of_d_radix

