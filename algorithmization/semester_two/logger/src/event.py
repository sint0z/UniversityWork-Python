from enum import Enum

# Перечисления, отвечающие за конкретный тип события
class LoggerEvent(Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    FATAL = "fatal" 

