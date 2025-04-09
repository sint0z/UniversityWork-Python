import os
import string

FOLDER = "second"
SUBFOLDER = "data"
FILE_NAME = "text.txt"
PATH = os.path.join(FOLDER,SUBFOLDER ,FILE_NAME)

def main():
    words = loading_file(PATH)
    unique_dict = unique_words(words)
    
    data = []
    with open(PATH, "r") as file:
        data = file.readlines()

        for line in data:
            
            for word in line:
                
                if word.lower() == "the":
                    print(word)
                    word = "THE_LARGE"

        with open(PATH, "w") as file:
                file.writelines(data)
          


def loading_file(path_to_file):
    arr = []
    with open(path_to_file) as file:
        data = file.readlines()
        for d in data:
            tab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            arr += d.lower().translate(tab).split()

    return arr

def unique_words(array_word):
    dict_unique_word = {}
    
    for word in array_word:
        if word in dict_unique_word:
            dict_unique_word[word]+= 1
        else:
            dict_unique_word[word] = 1
    return dict_unique_word


if __name__ == '__main__':
    main()
                
            
           
