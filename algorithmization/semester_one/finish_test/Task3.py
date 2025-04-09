text = input("Введите текст: ")

words = text.split()

total_words = 0
for word in words:
    total_words += 1

unique_words = []
for word in words:
    is_unique = True
    for unique_word in unique_words:
        if word == unique_word:
            is_unique = False
            break
    if is_unique:
        unique_words.append(word)

longest_word = ""
length_of_longest = 0

for word in words:
    word_length = 0
    
    for char in word:
        word_length += 1
    
    if word_length > length_of_longest:
        longest_word = word
        length_of_longest = word_length

print("Общее количество слов:", total_words)
print("Количество уникальных слов:", len(unique_words))
print("Самое длинное слово:", longest_word)
print("Длина самого длинного слова:", length_of_longest)
