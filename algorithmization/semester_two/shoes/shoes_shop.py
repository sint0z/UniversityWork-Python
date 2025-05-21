from client import Client
from shoes import Shoe
from typing import List, Tuple

class Shop:
    def __init__(self, shoes: List[Shoe] = []):
        self.__list_shoes: List[Shoe] = shoes

    def add_new_shoe(self, shoe: Shoe) -> None:
        self.__list_shoes.append(shoe)

    def pick_up_shoes(self, client: Client) -> Tuple[List[Shoe], int]:
    
        for shoe in self.__list_shoes:
            client.put_on(shoe)
                
        return client.put_on_list(), client.number_of_shoes()

                
        