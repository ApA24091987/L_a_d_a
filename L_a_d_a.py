first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assambler']

# Создание списка длин строк из first_strings с условием длины не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Создание списка пар слов с одинаковой длиной из first_strings и second_strings
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# Создание словаря с парами строк-длины строк из объединенных списков first_strings и second_strings
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
