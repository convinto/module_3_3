# Функция с параметрами по умолчанию:
def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()  # производит вывод параметров, заданных по умолчанию
print_params(b=25)  # производит замену параметра b
print_params(c=[1, 2, 3])  # производит замену параметра c на список

print()  # отступ

# Распаковка параметров:
values_list = [99, 'Hello', False]
values_dict = {'a': 66, 'b': [9, 8, 7, 6, 5], 'c': 'My name is Alexandr'}
print_params(*values_list)  # распаковка списка
print_params(**values_dict)  # распаковка словаря

# Распаковка + отдельные параметры:
values_list_2 = [{666, 777, 888}, 'Window']
print_params(*values_list_2, 42)  # функция работает и проивзодит распаковку списка с добавлением параметра
