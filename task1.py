def get_unique_names(mentors):
    # добавьте в список всех преподавателей со всех курсов
    all_list = []
    for m in mentors:
        for name in m:
            all_list.append(name)

    # сделайте список all_names_list, состоящий только из имен, и заполните его
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')[0]
        all_names_list.append(name)

    # сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
    unique_names = set(all_names_list)

    # теперь нужно отсортировать имена в алфавитном порядке. подсказка: используйте sorted() для списка
    # допишите код ниже
    all_names_sorted = sorted(unique_names)
    # допишите конструкцию вывода результата. можете использовать string.join()
    # результат будет в all_names_sorted
    sorted_unique_names = ', '.join(all_names_sorted)
    answer = f'Уникальные имена преподавателей: {sorted_unique_names}'
    return answer
