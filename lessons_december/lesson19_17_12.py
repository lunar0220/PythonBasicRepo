# # генетратор - это похожее на списки, некоторая конструкция, создается из функций. не возращает весь список
# nums = (i for i in range(1000))
# print(nums)


# # print(next(nums))
# # print(next(nums))
# # print(next(nums)).     так работает генератор

# for n in nums:
#     print(n)


# # функция генератора
# from typing import Generator
# def nums_generator(counter: int) -> Generator:
#     for i in range(counter):
#         yield i   #return для генераторов

# nums = nums_generator(5)

# for n in nums:
#     print(n)


# итераторы - он хранит все состояние коллекции

# nums = [1, 2, 3, 4, 5]

# iterator = iter(nums)

# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# for i in nums:     #итерируют
#     print(i)

# for i in range(len(nums)):     #цикл
#     print(nums[i])

# хз че за хуйня(конттекстный менеджер)
class FileWriter:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None


    def __enter__(self) -> "FileWriter":
        self.file = open(self.filename, "w")
        return self
    

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Error: {exc_value} Traceback{traceback}")
        self.file.close()
        return True
    

    def write(self, text: str) -> None:
        self.file.write(text)


with FileWriter("text.txt") as fw:
    fw.write("Goodbye, World!")

print()
print()