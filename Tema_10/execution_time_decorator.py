import csv
import time


def execution_time_measurement(func):
    def wrapper():
        start_time = time.time()
        time.sleep(1)
        end_time = time.time()
        elapsed_time = (end_time - start_time) - 1
        func()
        print(f'Execuction time:', elapsed_time, 'seconds')

    return wrapper


'''
@execution_time_measurement
def suma_primele_1mil_nr():
    sum_of_first_million_nr = 0
    for i in range(1000000):
        sum_of_first_million_nr += i
    print(f'The sum is equal with {sum_of_first_million_nr}')


suma_primele_1mil_nr()


'''


@execution_time_measurement
def lista1():
    lista = list(range(100))
    print(lista)


def gen_100_numbers(n):
    generated_numbers = 0
    while generated_numbers < n:
        yield generated_numbers
        generated_numbers += 1


@execution_time_measurement
def generator_of_100_numbers():
    for i in gen_100_numbers(100):
        print(i)


generator_of_100_numbers()
lista1()


# ex 3
def writer_decorator(file_name):
    def decorator_settings(func):
        def wrapper(*ints, **strings):
            name_of_function = f'The name of the function is:  {func.__name__}()'
            parameters_of_function = f'Its parameters are as follows: {str(func.__code__.co_varnames)}'
            results_of_function = f'And the results are:  {func(*ints, **strings)}'
            with open(file_name, 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name_of_function, parameters_of_function, results_of_function])

        return wrapper

    return decorator_settings


@writer_decorator('ex3.csv')
def client_data(name, salary, job):
    return f'Our client name is {name}, his salary is {salary}  and his job is  {job}'


@writer_decorator('ex3.csv')
def what_product_to_buy(name, id, price):
    return f'The right product for him is {name} with the id: {id} and with the price of {price}'


client_data('John Terry', 12000000, 'Footballer')
what_product_to_buy('Xbox', '1997473', '350 $')
