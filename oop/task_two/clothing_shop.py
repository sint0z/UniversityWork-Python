class Clothes:
    
    def __init__(self, fabric_cost_per_metr, fabric_length):
        self.__fabric_cost_per_metr = fabric_cost_per_metr
        self.__fabric_length = fabric_length

    def calculate_item_cost(self):
        return self.__fabric_cost_per_metr * self.__fabric_length
    
    def __repr__(self):
        return f"Количество ткани = {self.__fabric_length} \nCтоимость единицы длинны = {self.__fabric_cost_per_metr}"
        
    def display(self):
        print(self)


class Atelier:

    def __init__(self, clothes_dict: dict, accessories_cost: int):
        self.__clothes_dict = clothes_dict
        self.__accessories_cost = accessories_cost


    def display(self):
        print("Список одежды: \n")

        for i, (clothes, quantity) in enumerate(self.__clothes_dict.items(), start=1):
            if isinstance(clothes, Clothes):
                print(f"Одежда № {i}")
                clothes.display()
                print(f"Количество в ателье: {quantity} \n")

        total_cost = self.calculate_total_cost()
        most_expensive_cost = self.find_most_expensive_clothing()

        print(f"Общая стоимость продукции в ателье: {total_cost}")
        print(f"Самый дорогой товар стоит: {most_expensive_cost}")


    def calculate_total_cost(self):
        total_clothes_cost = self.__accessories_cost

        for clothes, quantity in self.__clothes_dict.items():
            if(isinstance(clothes, Clothes)):
                total_clothes_cost += clothes.calculate_item_cost() * quantity

        return total_clothes_cost
    

    def find_most_expensive_clothing(self):
        max_cost = 0

        for clothes in self.__clothes_dict.keys():
            if(isinstance(clothes, Clothes)):
                print(clothes.calculate_item_cost())
                if(max_cost < clothes.calculate_item_cost()):
                    max_cost = clothes.calculate_item_cost()
                    
        return max_cost


if __name__ == "__main__":

    clothes = {
        Clothes(213, 5): 5,
        Clothes(100, 10): 10,
        Clothes(55, 7): 70
    }

    atelier = Atelier(clothes, 1200)
    atelier.display()
    

    
  