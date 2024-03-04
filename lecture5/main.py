data_stream = [2,3,4,8,9,1,5,6]
search_number = int(input("Zadaj cislo"))
index = 0
while not(data_stream[index]==search_number):
    index+=1
print(index)