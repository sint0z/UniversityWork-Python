import re

# Класс для хранения даты в, числовом эквиваленте
# Создан как вспомогательный дабы не использовать встроенный в Python
# C какой-то стороны объекты класса выступают как DTO

class Date:

    def __init__(self, year: int = None, month: int = None, day: int=None):
        self.year: int = year
        self.month: int = month
        self.day: int = day

    @staticmethod
    def generateDate(date_str: str) -> 'Date':
        separate = r"[.\-\/]"
    
        parts = re.split(separate, date_str)
        parts = [p.strip() for p in parts if p.strip()]

        if len(parts) != 3:
            raise ValueError("Неверно указана дата: (ГОД|МЕСЯЦ|ДЕНЬ)")
        
        nums = list(map(int, parts))


        year = None
        for n in nums:
            if 1000 <= n <= 9999:
                year = n
                break
        if year is None:
            raise ValueError("Год не найден в дате")
        

        others = [n for n in nums if n != year]
        
        month = None
        day = None
        
        for n in others:
            if 1 <= n <= 12 and month is None:
                month = n
            elif 1 <= n <= 31 and day is None:
                day = n
        
        if month is None or day is None:
            if all(1 <= n <= 12 for n in others):
                month, day = others[0], others[1]
            else:
                month, day = others[0], others[1]
        
        return Date(year, month, day)
    
    def __eq__(self, other):
        if not isinstance(other, Date):
            return False
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __repr__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"