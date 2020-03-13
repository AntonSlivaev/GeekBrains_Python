def my_function(a,b) :
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return 'b не должен быть нулевым '
    except ValueError:
        return 'вы ввели не число'
print(my_function(int(input('введите а = ')), int(input('введите b = '))))