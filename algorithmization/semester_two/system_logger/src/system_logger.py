from typing import Tuple, List;
from level_errors import LevelErrors
from date import Date
import csv

class SystemLogger:
    def __init__(self):
        self.__logs: List[Tuple[LevelErrors, Date, str, str ]] = []


    def __create_tuple(self, level, *data) -> Tuple:
        return (level, *data)
    

    def log(self, level: LevelErrors, date: Date, time: str,  description: str) -> None:
        temp_date = None
        if isinstance(date, str):
            temp_date = Date.generateDate(date)            
        elif isinstance(date, Date):
            temp_date = date
        else:
            raise ValueError("Дата не указана или неверного типа")
        self.__logs.append(self.__create_tuple(level, temp_date, time, description))
    

    def search(self, date: str) -> List[Tuple]:
        try:
            search_date = Date.generateDate(date)
        except Exception as e:
            print(f"Произошла ошибка в парсинге даты: {e}")
            return []
        return [res for res in self.__log if res[1] == search_date]
    

    def print(self) -> None:
        for rec in self.__logs:
            level, date, time , description = rec
            print(f"[{date}] | {level.value} | Time: {time} | Description: {description}")

    
    def filter_by_event(self, event: LevelErrors) -> List[Tuple]:
        return [res for res in self.__logs if res[0] == event]
     

    def delete(self, date: Date) -> bool:
        try:
            target_date = Date.generateDate()
        except Exception as e:
            print(f"Ошибка при парсинге даты: {e}")
            return False
        for idx, rec in enumerate(self._list_tuple):
             if rec[1] < target_date:
                del self.__logs[idx]
                return True
        return False
    

    def save_to_csv(self, file_name: str) -> None:
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["level", "date", "time" ,"description"])

            for res in self.__logs:
                level, date, time, description = res
                writer.writerow([level.name, date, time, description])


logger = SystemLogger()
logger.log(LevelErrors.ERROR, "2025-04-22", "10:00", "Test description")
logger.save_to_csv("file.csv")
print(logger.filter_by_event(LevelErrors.ERROR))