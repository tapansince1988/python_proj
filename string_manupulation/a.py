def sum_of_nums(string_val):
    sum = 0
    for element in string_val:
        if(element.isdigit()):
            sum += int(element)
    return sum

print('Enter string using alphanumeric : ')

input_string = str(input())

print(sum_of_nums(input_string))

# 1abc23@c$64-zy5~4dfg#235
# 1+23+64+5+4+235 = ?
# answer = 335