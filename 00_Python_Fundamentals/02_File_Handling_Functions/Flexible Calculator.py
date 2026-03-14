def calculator(*args):
    output_sum = sum(args)
    output_average = output_sum / len(args)
    output_maximum = max(args)
    return output_average, output_maximum, output_sum

print(calculator(1,2,3,4,5,6,7,8,9))