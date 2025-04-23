from collections import defaultdict

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

word = "Test"
score = scrabble_score(word) 
print(f"Score: {score} for word {word} \n")


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

email_list = generate_emails(emails)


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


