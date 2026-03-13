my_list = [1,2,3,4,5,6,7,8,9,10]
gen_list =  (n**2 for n in my_list)
for i in range(5):
    print(next(gen_list))