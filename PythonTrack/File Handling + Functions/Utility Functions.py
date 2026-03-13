
def average(num):
    sum_of_list = sum(num)
    return sum_of_list/len(num)

def maximum(num):
    maximum = max(num)
    return maximum

def compare(num,value):
  count =0
  for number in num:
      if number > value:
          count +=1
  return "Greater number: ",count

list1=[1,2,3,4,5,6]
print(average(list1))
print(maximum(list1))
print(compare(list1,5))
