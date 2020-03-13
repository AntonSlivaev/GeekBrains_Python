def my_function(x, y, z):
    list = [x, y, z]
    total= []
    max_1 = max(list)
    total.append(max_1)
    list.remove(max_1)
    max_2 = max(list)
    total.append(max_2)
    print(sum(total))

my_function(1, 3, 5)