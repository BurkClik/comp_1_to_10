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