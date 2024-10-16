from Store import Store
from TaskManager import TaskManager


def create_stores():
    store_first = Store("Фруктовый Рай", "ул. Ленина, д. 10")
    store_first.add_item("Яблоки", 0.5)
    store_first.add_item("Бананы", 0.75)
    store_first.add_item("Апельсины", 0.6)

    store_second = Store("Электроника Плюс", "пр. Мира, д. 20")
    store_second.add_item("Смартфон", 299.99)
    store_second.add_item("Ноутбук", 799.99)
    store_second.add_item("Наушники", 49.99)

    store_third = Store("Книжный Мир", "ул. Советская, д. 5")
    store_third.add_item("Роман", 15.99)
    store_third.add_item("Учебник по Python", 45.50)
    store_third.add_item("Журнал", 5.99)

    return store_first, store_second, store_third


if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Написать отчет", "2024-05-01")
    manager.add_task("Подготовить презентацию", "2024-04-25")
    manager.add_task("Встреча с клиентом", "2024-04-20")

    # Вывод текущих задач
    manager.list_current_tasks()

    # Отметка задачи как выполненной
    manager.mark_task_completed("Подготовить презентацию")

    # Вывод текущих задач после обновления статуса
    manager.list_current_tasks()

    # Создание магазинов
    store1, store2, store3 = create_stores()

    # Вывод информации о магазинах
    print(store1)
    print(store2)
    print(store3)

    # Выбор одного магазина для тестирования (например, store1)
    selected_store = store1
    print(f"\nТестирование методов магазина: {selected_store.name}")

    # Добавление товара
    selected_store.add_item("Груши", 0.8)

    # Обновление цены товара
    selected_store.update_price("Бананы", 0.85)

    # Удаление товара
    selected_store.remove_item("Апельсины")

    # Запрос цены товара
    price = selected_store.get_price("Яблоки")
    if price is not None:
        print(f"Цена за 'Яблоки': {price}")
    else:
        print("Товар 'Яблоки' не найден.")

    # Запрос цены отсутствующего товара
    price = selected_store.get_price("Апельсины")
    if price is not None:
        print(f"Цена за 'Апельсины': {price}")
    else:
        print("Товар 'Апельсины' не найден.")

    # Вывод обновленного состояния магазина
    print("\nОбновленный ассортимент магазина:")
    print(selected_store)
