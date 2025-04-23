from collections import defaultdict

# Задача 1.
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# •	A, E, I, O, U, L, N, S, T, R – 1 очко;
# •	D, G – 2 очка;
# •	B, C, M, P – 3 очка;
# •	F, H, V, W, Y – 4 очка;
# •	K – 5 очков;
# •	J, X – 8 очков;
# •	Q, Z – 10 очков.
# А русские буквы оцениваются так:
# •	А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# •	Д, К, Л, М, П, У – 2 очка;
# •	Б, Г, Ё, Ь, Я – 3 очка;
# •	Й, Ы – 4 очка;
# •	Ж, З, Х, Ц, Ч – 5 очков;
# •	Ш, Э, Ю – 8 очков;
# •	Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
def scrabble_score(word: str) -> int:
    rus_char  = {
        "АВЕИНОРСТ" : 1, 
        "ДКЛМПУ" : 2,
        "БГЁЬЯ" : 3,
        "ЙЫ" : 4,  
        "ЖЗХЦЧ": 5,
        "ШЭЮ" : 8,
        "ФЩЪ" : 10 
    }   

    eng_char = {
        "AEIOULNSTR" : 1,
	    "DG" : 2,
    	"BCMP" : 3,
    	"FHVWY" : 4,
    	"K" : 5,
    	"JX": 8,
    	"QZ" : 10,
    }

    current = {}
    if word[0].upper() in  " ".join(rus_char.keys()):
        current = rus_char
    elif word[0].upper() in " ".join(eng_char.keys()):
        current = eng_char
    
    total_cost = 0
    for char in word:
        for key, cost in current.items():
            if char.upper() in key:
                total_cost += cost
                break

    return total_cost
	
# Задание 1 - Тестирование
word = "Test"
score = scrabble_score(word) 
print(f"Score: {score} for word {word} \n")


# Задача 2
# Данные об email-адресах студентов хранятся в словаре
# Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен.
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}


def generate_emails(emails_map: dict[str, list[str]]) -> list[str]:
    emails: list[str] = list()

    for domain, users in emails_map.items():
        for user in users:
            emails.append("{0}@{1}".format(user,domain))
    return emails
	
# Задание 2- Тестирование
email_list: list = generate_emails(emails)
email_list.sort()
print(email_list)

# Задача 3
# Напишите функцию, которая принимает два кортежа, объединяет их и возвращает новый кортеж без повторяющихся элементов.
tupleOne = (1, 2)
tupleTwo = (2, 5)
def concatenate_tuple(tupleOne: tuple, tupleTwo: tuple) -> tuple:
    return set(tupleOne + tupleTwo)


new_tuple = concatenate_tuple(tupleOne, tupleTwo)

print(f"Tuple one -> {tupleOne}")
print(f"Tuple two -> {tupleTwo}")
print("New Tuple -> " + str(new_tuple) + "\n")



data = [("Москва", 2020, 12_000_000),
    ("Санкт-Петербург", 2020, 5_400_000),
    ("Москва", 2021, 12_200_000),
    ("Санкт-Петербург", 2021, 5_350_000)]

population_by_city = defaultdict(int)

for city, _, population in data:
        population_by_city[city] += population

for city, total_population in population_by_city.items():
    print(f"Город: {city} -> Численность: {total_population}")


