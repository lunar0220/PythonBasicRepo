# # мультипоточность
# import threading
# import time

# def print_nums(name: str) -> None:
#     for i in range(1, 11):
#         print(f"Thread: {name} nums: {i}")
#         time.sleep(1)



# thread_1 = threading.Thread(target=print_nums, args=("thread_1",))
# thread_2 = threading.Thread(target=print_nums, args=("thread_2",))

# print("Поток запущен")
# thread_1.start()
# thread_2.start()

# thread_1.join() можно не писать
# thread_2.join()


# import threading
# locker = threading.Lock()
# counter = 0

# def increment() -> None:
#     global counter
#     for _ in range(10000):
#         with locker:
#             counter += 1


# threads = [threading.Thread(target=increment) for _ in range(5)]

# for th in threads:
#     th.start()


# for th in threads:
#     th.join()


# print(f"Counter: {counter}")




# асинхронное программиррованние
print()

import asyncio
import time

async def task_1() -> None:
    await asyncio.sleep(2)
    return "task_1 completed"


async def task_2() -> None:
    await asyncio.sleep(2)
    return "task_2 completed"


async def task_3() -> None:
    for _ in range(100000000):
        continue
    # await asyncio.sleep(2)
    return "task_3 completed"


async def main() -> None:
    start = time.time()
    results = await asyncio.gather(task_1(), task_2(), task_3())
    print( results)
    end = time.time()
    print(f"Time : {end - start}")

asyncio.run(main())


# мультипроцессерность