from shoes import Shoe
from typing import List

class Client:
    def __init__(self, name: str, hand_size: int):
        self.__name: str = name
        self.__hand_size: int = hand_size
        self.__hand: Shoe = None


    def try_it(self, shoe: Shoe)-> bool:
        return self.__hand_size == shoe.size() 
    

    def put_on(self, shoes: Shoe) -> bool:
        if self.__hand is None:
            if(self.try_it(shoes)):
                self.__hand = shoes
                return True
        else:
            self.__hand.put_on_another(shoes)
            return True
        return False
    

    def put_on_list(self) -> List[Shoe]:
        shoe: Shoe = self.__hand
        list_shoe: List[Shoe] = []

        while(shoe is not None):
            list_shoe.append(shoe)
            shoe = shoe.next
        
        return list_shoe


    def number_of_shoes(self) -> int:
        return len(self.put_on_list())
    
    
    def statistic(self) -> None:
        print(f"Client '{self.__name}', hand size: [{self.__hand_size}]")


        
            