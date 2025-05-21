from random import randint
from shoes_shop import Shop
from shoes import Shoe
from client import Client

RANGE_OF_SIZE = (35, 47)


def main():
    min_size, max_size = RANGE_OF_SIZE
    
    shoe_shop: Shop = Shop()
    
    for i in range(1000):
        size = randint(min_size, max_size) + 1 
        name_shoe: str = f"Shoe №{i} - [{size}]"
        shoe_shop.add_new_shoe(Shoe(name_shoe, size))


    client: Client = Client("Client_1", randint(min_size, max_size))
    client.statistic()

    list_shoes,count_pair = shoe_shop.pick_up_shoes(client)
    
    print("Result: ")
    print(f"{"":1}-> The client was able to wear {count_pair} pairs:")
    if list_shoes:
        for i, shoe in enumerate(list_shoes):
            print(f"{"":3}{i:2}." + str(shoe))


if __name__ == "__main__":
    main()