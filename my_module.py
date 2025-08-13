PI = 3.14
def summa(a: int, b: int) -> int:
    '''
    Функция суммирует два числа
    '''
    return a + b


if __name__ == '__main__':
    print("Самостоятельный запуск")
else:
    print(__name__, "Импортированный модуль")