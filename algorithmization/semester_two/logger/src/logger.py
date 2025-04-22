from event import LoggerEvent
from date import Date
from typing import List, Tuple, Optional
from pathlib import Path

class Logger():

    # Временное решение, путь до папки "data" в проекте
    current_dir = Path(__file__).parent
    data_dir = current_dir.parent / 'data'

    def __init__(self):
        self._list_tuple:List[Tuple[str, Date, str, LoggerEvent, str]] = []

    # Вспомгательный метод для создания кортежей
    def __create_tuple(self,uid, *data,) -> Tuple:
        return (uid, *data)
    
    # Создайте кортеж, который будет хранить информацию о записи журнала, включая дату, время, тип события, описание и user_id.
    # Добавление записей в журнал
    def log(self, uid:str, date, time: str, event: LoggerEvent, description: str) -> None:
        temp_date = None
        if isinstance(date, str):
            temp_date = Date.generateDate(date)            
        elif isinstance(date, Date):
            temp_date = date
        else:
            raise ValueError("Дата не указана или неверного типа")
        self._list_tuple.append(self.__create_tuple(uid, temp_date, time, event, description))
    

    # Вывод записей журнала
    def print(self) -> None:
        for rec in self._list_tuple:
            uid, date, time, event, description = rec
            print(f"UID: {uid} | Date: {date} | Time: {time} | Event: {event.value} | Description: {description}")


    # Поиск записей по дате
    def search(self, date: str) -> List[Tuple]:
        try:
            search_date = Date.generateDate(date)
        except Exception as e:
            print(f"Произошла ошибка в парсинге даты: {e}")
            return []
        return [res for res in self._list_tuple if res[1] == search_date]
    

    # Фильтрация записей по типу события
    def filter_by_event(self, event_type: LoggerEvent) -> List[Tuple]:
        return [res for res in self._list_tuple if res[3] == event_type]
    

    # Обновление записи журнала
    def update(self, uid: str, date_str: str, time: str, new_event: Optional[LoggerEvent] = None, new_description: Optional[str] = None) -> bool:
        try:
            target_date = Date.generateDate(date_str)
        except Exception as e:
            print(f"Произошла ошибка в парсинге даты: {e}")
            return []
        
        for idx, entry in enumerate(self._list_tuple):
            if entry[0] == uid and entry[1] == target_date and entry[2] == time:
                uid_, date_, _, event_, description_ = entry
                event_ = new_event if new_event else event_
                description_ = new_description if new_description else description_
                self._list_tuple[idx] = (uid_, date_, time, event_, description_)    
                return True
        return False


    # Удаление записи журнала
    def delete(self, uid: str, date_str: str, time: str) -> bool:
        try:
            target_date = Date.generateDate(date_str)
        except Exception as e:
            print(f"Ошибка при парсинге даты: {e}")
            return False
        for idx, rec in enumerate(self._list_tuple):
            if rec[0] == uid and rec[1] == target_date and rec[2] == time:
                del self._list_tuple[idx]
                return True
        return False


    # Сортировка по "date" ил "time"
    def sort(self, by: str = "date") -> None:
        if by == "date":
            self._list_tuple.sort(key=lambda r: (r[1].year, r[1].month, r[1].day, r[2]))
        elif by == "time":
            self._list_tuple.sort(key=lambda r: (r[2], r[1].year, r[1].month, r[1].day))
        else:
            raise ValueError("Параметр сортировки должен быть 'date' или 'time'")


    # Запись в файл
    def write_to_file(self, filename: str) -> None:
        with open(Logger.data_dir / filename, "w") as f:
            for rec in self._list_tuple:
                uid, date, time, event, description = rec
                
                line = f"{uid}|{date}|{time}|{event.value}|{description}\n"
                f.write(line)


    # Чтение из файла
    def read_to_file(self, filename: str) -> None:
        with open(Logger.data_dir / filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split("|")

                if len(parts) != 5:
                    continue

                uid, date, time, event_str, description = parts

                try: 
                    date = Date.generateDate(date)
                except Exception as e:
                    print(f"Ошибка при парсинге даты: {e}")
                    continue
                
                try:
                    event = LoggerEvent(event_str)
                except Exception as ex:
                    print(f"Ошибка неверно указано событие {event_str}")

                self.log(uid, date, time, event, description)
            


    