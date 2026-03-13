data = [10,20,10,30,40,20,50]

mapper = set()
final_output = []

for elements in data:
    if elements not in mapper:
        mapper.add(elements)
        final_output.append(elements)
print("Final Output: ",final_output)
