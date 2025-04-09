
# Задание № 1
def merge_two_dict1(dict1:dict, dict2:dict) -> dict:

    for key in dict2.keys():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance[dict[key], dict]:
                merge_two_dict1(dict1[key], dict2[key])

            elif dict1[key] != dict2[key]:
                dict1[key] =  dict2[key]
        else:
            dict1[key] = dict2[key]    
    return dict1


def merge_two_dict2(dict1:dict, dict2:dict) -> dict:
    return dict1 | dict2 if dict1 and dict2 else {}


dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print("----------Вывод задания #1--------------")
print(merge_two_dict1(dict_1, dict_2))
print(merge_two_dict2(dict_1, dict_2))
print("----------------------------------------\n")


# Задание № 2
def max_dict(*dicts:dict) -> dict:
    result = dict()

    for d in dicts:
        for key in d.keys():
            if key in result:
                if result[key] != d[key]:
                    result[key] = max(result[key], d[key])
            else: 
                result[key] = d[key]    
    return result


def sum_dict(*dicts:dict) -> dict:
    result = dict()

    for d in dicts:
        for key in d.keys():
            if key in result:
                result[key] += d[key]
            else:
                result[key] = d[key]
    return result


dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

print("----------Вывод задания #2--------------")
print(max_dict(dict_1, dict_2))
print(sum_dict(dict_1, dict_4, dict_3))
print(max_dict(dict_1, dict_2, dict_3, dict_4))
print(sum_dict(dict_1, dict_2, dict_3, dict_4))
print("----------------------------------------\n")

#Задание 3
def set_gen(list_number: list) -> set:
    counts = dict()
    s = set()
    
    for num in list_number:
        counts[num] = counts.get(num, 0) + 1 
        count = counts[num]
        s.add(count if count == 1 else str(num)*count)
    return s

print("----------Вывод задания #3--------------")
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))
print("----------------------------------------\n")


# Задание 4
def superset(set_a:set, set_b:set) -> None:
    if set_a == set_b:
        print("Множества равны")
    elif set_a.issuperset(set_b) and len(set_a) > len(set_b):
        print(f"Объект {set_a} является чистым супермножеством")
    elif set_b.issuperset(set_a) and len(set_b) > len(set_a):
        print(f"Объект {set_b} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

print("----------Вывод задания #4--------------")
set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)
print("----------------------------------------\n")