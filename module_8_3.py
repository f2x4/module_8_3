class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    @classmethod
    def __is_valid_numbers(cls, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(
                message='Некорректный тип данных для номеров'
            )
        if len(numbers) != 6:
            raise IncorrectCarNumbers(message='Неверная длина номера')
        return True

    @classmethod
    def __is_valid_vin(cls, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber(message='Некорректный тип vin номер')
        if 1000000 > vin and vin < 9999999:
            raise IncorrectVinNumber(
                message='Неверный диапазон для vin номера'
            )
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 3000, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')