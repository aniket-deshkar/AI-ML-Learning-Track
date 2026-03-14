#Task 14 - Prime, Perfect, Armstrong
total_prime_number = 0
total_perfect_number = 0
total_armstrong_numbers =0
for i in range(1,500):
    #Prime Numbers
    if i<2:
        continue
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print(i," is Prime | ")
        total_prime_number = total_prime_number + 1

    #Perfect Numbers
    sum_of_numbers = 0
    for k in range(1, i):
        if i % k == 0:
            sum_of_numbers = sum_of_numbers + k
    if sum_of_numbers == i:
        print(i, "is Perfect | ")
        total_perfect_number = total_perfect_number + 1


    # 3. ARMSTRONG CHECK (Power of digits)
    no_of_digits = str(i)
    power = len(no_of_digits)
    armstrong_sum = 0
    for d in no_of_digits:
        armstrong_sum = armstrong_sum + (int(d) ** power)
    if armstrong_sum == i:
        print(i, " is Armstrong |")
        total_armstrong_numbers = total_armstrong_numbers + 1

print("Total Prime numbers are ", total_prime_number)
print("Total Perfect numbers are ", total_perfect_number)
print("Total Armstrong numbers are ", total_armstrong_numbers)



