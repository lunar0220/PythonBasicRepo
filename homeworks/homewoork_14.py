import asyncio

async def send_notification(user:str, delay:int) -> None:
    print(f"Начинаю отправку уведомления для {user}...")
    await asyncio.sleep(delay)
    print(f"Уведомление для {user} отправлено!")

async def main() -> None:
    users = [
        ("Alice", 2),
        ("Bob", 3),
        ("Charlie", 1),
        ("Diana", 4)
        ]
    tasks = [
        asyncio.create_task(send_notification(user, delay))
        for user, delay in users
    ]

    await asyncio.gather(*tasks)

    print(f"Все уведомления отправлены.")

if __name__ == "__main__":
    asyncio.run(main())