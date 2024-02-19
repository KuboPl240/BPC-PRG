my_car = "bugatti, divo, 2018, 34562876, 9845284635, blue, True"
my_car_list = list()
for i in list(my_car.split(", ")):
    if isinstance(i, int):
      my_car_list.append(int(i))
    else:
        my_car_list.append(i)

print(my_car_list)
