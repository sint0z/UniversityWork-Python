from enum import Enum

# Перечисления, отвечающие за конкретный тип события
class LevelEvent(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    FATAL = 50 

