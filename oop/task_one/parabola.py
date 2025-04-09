import math

class Parabola:
    def __init__(self, _a = 0, _b = 0, _c = 0):
         self.field_a = _a
         self.field_b = _b
         self.field_c = _c
      
    def get_field_a(self):
        return self.field_a
    
    def get_field_b(self):
        return self.field_b
    
    def get_field_c(self):
        return self.field_c
    
    def read(self):
        while True:
            try:
                self.field_a = int(input("Введите первый коэффициент а (не равный 0): "))

                if(self.field_a == 0):
                    print("Коэффициент а не может быть равен нулю")
                    continue
                
                self.field_b = int(input("Введите первый коэффициент b: "))
                self.field_c = int(input("Введите первый коэффициент c: "))
                break
            except ValueError:
                print("Ошибка ввода: Введите числовое значение !")
        return self

    def display(self):
        print(f"Парабола {self.field_a}*x^2 + {self.field_b}*x + {self.field_c}")


    def __add__(self, other):
        if isinstance (other, Parabola):
            a = other.get_field_a() + self.field_a
            b = other.get_field_b() + self.field_b
            c = other.get_field_c() + self.field_c
        return Parabola(a,b,c)

    def distance_to_origins(self):
        x_v = - self.field_b / (2 * self.field_a)
        y_v = self.field_c  - (self.field_b**2) / (4 * self.field_a)
        
        return math.sqrt(x_v**2 + y_v**2)
    
    
def main():
    print("Парабола 1")
    parabola_one = Parabola()
    parabola_one.read()

    print("Парабола 1")
    parabola_two = Parabola()
    parabola_two.read()

    parabola_one.display()
    parabola_two.display()

    distance = parabola_one.distance_to_origins()
    print(f"Расстояние от вершины параболы до начала координат: {distance}")


    parabola_three = parabola_one + parabola_two
    if(isinstance(parabola_three, Parabola)):
        parabola_three.display()


if __name__ == "__main__":
    main()