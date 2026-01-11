# import threading
# import time
#
#
# def print_numbers(name: str) -> None:
#     for i in range(1, 11):
#         time.sleep(1)
#         print(f"Thread: {name} Number: {i}")
#
# thread_1 = threading.Thread(target=print_numbers, args=("thread_1",))
# thread_2 = threading.Thread(target=print_numbers, args=("thread_2",))
#
# thread_1.start()
# thread_2.start()
# print("Поток запущен!")
#
# thread_1.join()
# thread_2.join()

#
# import threading
# import time
#
# counter = 0
#
#
# locker = threading.Lock()
#
#
# def increment() -> None:
#     global counter
#     for _ in range(100000):
#         with locker:
#             counter += 1
#
#
# threads = [threading.Thread(target=increment) for _ in range(5)]
#
# for th in threads:
#     th.start()
#
# for th in threads:
#     th.join()
#
# print(f"Counter: {counter}")

import asyncio
import time


async def task_1() -> str:
    await asyncio.sleep(2)
    return "Task 1 comleted"


async def task_2() -> str:
    await asyncio.sleep(2)
    return "Task 2 comleted"


async def task_3() -> str:
    await asyncio.sleep(2)
    return "Task 3 comleted"


async def async_main() -> None:
    start = time.time()
    results = await asyncio.gather(task_1(), task_2(), task_3())
    end = time.time()
    print(results)
    print(f"Time - {end-start}")


def main(name: str, sleep_time: int):
    print(f"Process: {name} started")
    time.sleep(sleep_time)
    asyncio.run(async_main())
    print(f"Process: {name} ended")


import multiprocessing


if __name__ == "__main__":
    process_1 = multiprocessing.Process(
        target=main,
        args=("process_1", 5),
        daemon=True
    )
    process_1.start()
    main("main", 3)
    process_1.join()