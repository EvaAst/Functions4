"""
 Функция создает красивый резделитель из 10-и звездочек (**********)
 :return: **********
 """


def simple_separator(long=10, stars="*"):
    return (stars * long)


print(simple_separator())
print(simple_separator() == '**********')  # True
"""
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    """


def long_separator(count, stars="*"):
    return (stars * count)
    pass


print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True

"""
   Функция создает разделитель из любых символов любого количества
   """


def separator(simbol, count):
    return (simbol * count)
    pass


print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True
"""
   Функция печатает Hello World в формате:
   **********
   Hello World!
   ##########
   """


def hello_world(count=10):
    text = 'Hello World!'
    print('*' * count)
    print(text)
    print('#' * count)
    return
    pass


hello_world()


# Функция печатает приветствие в красивом формате

def hello_who(who='World', count=10):
    text = 'Hello'
    print('*' * count)
    print(text, who, '!')
    print('#' * count)
    return
    pass


hello_who('Max')
hello_who('Kate')


# Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)

def pow_many(power=1, *args):
    result = 0
    for number in args:
        result = number + result  # result = result + number
    return (result ** power)


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


# Функция выводит переданные параметры в фиде key --> value

def print_key_val(arrow="-->", **kwargs):
    for key, value in kwargs.items():
        print(key, arrow, value)
    return


print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)
