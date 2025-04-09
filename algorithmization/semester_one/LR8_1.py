import os

FOLDER = "university_task//data"
FILE_NAME = "winning_table.txt"
PATH = os.path.join(FOLDER, FILE_NAME)


def main():
   if os.path.exists(PATH):
    winnings = loading_winnings(PATH)

    ticket = input("Введите номер лотерейного билета:")
    winning = check_ticket(winnings, ticket)

    if winning:
            winning_str = " и ".join(map(str,winning))
            print(f"Билет с номером {ticket} выиграл {winning_str}")
    else:
            print(f"Билет с номером {ticket} не выигрышный ")   
   else:
       print("File is not found")
   
def loading_winnings(path_to_file):
    winnings = {}

    with open(path_to_file) as file:
        datas =  file.readlines()
        for data in datas:
            key,value = data.strip().split(" - ")
            winnings[key.strip()] = value.strip()
            
    return winnings   


def check_ticket(winnings,ticket):
    result = []
    for key,value in winnings.items():
        if ticket.endswith(key):
            result.append(value)
    return result


if __name__ == '__main__':
    main()