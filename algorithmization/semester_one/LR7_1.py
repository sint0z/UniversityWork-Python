import string

def frequently_encountered_symbol(arr_word):
    c = dict()

    for i in range(len(arr_word)):
        for symbol in arr_word[i]:
            c[symbol] = c.get(symbol,0) + 1

    return max(c.items(), key=lambda item:item[1])[0]
    

def max_word_fraction(arr_word,symbol):
    word = ""
    max_fraction = 0

    for wrd in arr_word:
        fraction = wrd.count(symbol)/len(wrd)

        if(fraction > max_fraction):
            max_fraction = fraction
            word = wrd

    return [word,max_fraction]

if __name__ == "__main__":
    text = "Veni, scripsi; vixi"
    tab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    arr_word = text.lower().translate(tab).split()
    max_symbol = frequently_encountered_symbol(arr_word)
    word = max_word_fraction(arr_word,max_symbol)

    print("Наиболее часто встречающийся символ - '", max_symbol,"'")
    if word != "":
        print("Слово в котором доля этого символа максимальна: ",word[0]," (",word[1],")")
    else:
        print("В предложении нет слов с данной буквой")
