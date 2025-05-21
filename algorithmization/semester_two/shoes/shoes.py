class Shoe:
    def __init__(self,name: str, size: int):
        self.__name: str = name
        self.__size: int = size
        self.next = None

    def put_on_another(self, shoes):
        if(isinstance (shoes, Shoe)):
            if(self.__size < shoes.size()):
                self.next = shoes
        else:
            raise ValueError("Вводимы класс не соответствует классу Shoes")
        
    def size(self):
        return self.__size
    
    def get_name(self):
        return self.__name
    

    def __repr__(self):
        return f"Shoe: {self.get_name()}[{self.size()}]"