class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()








# Итераторы
# Пример 1 - библиотека itertools
# import sys
# from itertools import repeat
#
#
# ex_iterator = repeat('4', 100_000)
# print(ex_iterator)
# print(f' the size of the iterator is- {sys.getsizeof(ex_iterator)}')
#
#
# ex_str = '4' * 100_000
# print(f'the size of the list is - {sys.getsizeof(ex_str)} ')


# Пример 2
#
# class Iter:
#     def __init__(self):
#         self.first = 'First element'
#         self.second = 'Second element'
#         self.third = 'Third element'
#         self.i = 0
#
#     def __iter__(self):
#         # Обнуляем счетчик перед циклом
#         self.i = 0
#         # Возвращаем ссылку на себя, так как сам объект должен быть итератором
#         return self
#
#     def __next__(self):
#         # Этот метод возвращает значения по требованию python (ленивые вычисления)
#         self.i += 1
#         if self.i == 1:
#             return self.first
#         if self.i == 2:
#             return self.second
#         if self.i == 3:
#             return self.third
#         if self.i == 4:
#             return 'Подсчет окончен'
#         raise StopIteration()   # Признак того, что больше возвращать нечего
#
#
# obj = Iter()
# print(obj)
#
# for value in obj:
#     print(value)
