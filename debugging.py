import logging
import colorlog

# logging.basicConfig(level=logging.DEBUG)

# настройка цветного логирования
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.propagate = False  # отключаем передачу в родительский логгер

# некритические ошибки
# logger.debug("Подробная информация для отладки")           # DEBUG
# logger.info("Информационное сообщение")

# # критические ошибки
# logger.warning("Предупреждение")                           # ERROR
# logger.error("Ошибка")
# logger.critical("Критическая ошибка")


def add_numbers(a: int,b: int) -> int:
    logger.info(f"Сложение чисел: {a} и {b}")
    return a + b

logger.debug("Программа запущена")
result = add_numbers(5, 3)
logger.info(f"Результат: {result}")

result = add_numbers(10, 20)
name = 'John'