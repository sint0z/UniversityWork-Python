from logger import Logger
from event import LoggerEvent

# Данну работу выполнил Стоцкий Никита (ПИЭ-42)
# Для выполнения работы использовались классы

if __name__ == "__main__":
    logger = Logger()
    logger.log("user1", "2025-04-22", "10:00", LoggerEvent.INFO , "User logged in")
    logger.log("user2", "22.04.2025", "11:00", LoggerEvent.ERROR, "Failed login")
    logger.log("user3", "2025-04-23", "09:30", LoggerEvent.WARNING, "Password will expire soon")
    logger.log("user4", "23-04-2025", "12:00", LoggerEvent.DEBUG, "Debug session started")

    print("Все записи журнала:")
    logger.print()

    print("\nПоиск по дате '2025-04-22':")
    for rec in logger.search("2025-04-22"):
        print(rec)

    print("\nФильтрация по событию 'error':")
    for rec in logger.filter_by_event(LoggerEvent.ERROR):
        print(rec)

    print("\nОбновление записи user2:")
    updated = logger.update("user2", "22.04.2025", "11:00", new_description="Multiple failed login attempts")
    print("Обновлено:", updated)
    logger.print()

    print("\nУдаление записи user4:")
    deleted = logger.delete("user4", "23-04-2025", "12:00")
    print("Удалено:", deleted)
    logger.print()

    print("\nСортировка по дате:")
    logger.sort("date")
    logger.print()

    filename = "logfile.txt"
    logger.write_to_file(filename)
    print(f"\nЛоги записаны в файл {filename}")

    new_logger = Logger()
    new_logger.read_to_file(filename)
    print("\nЛоги после чтения из файла:")
    new_logger.print()