class Store:
    def __init__(self, name, address):
        """
        Инициализация нового магазина.

        :param name: Название магазина.
        :param address: Адрес магазина.
        """
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def __str__(self):
        """Возвращает строковое представление магазина."""
        items_str = ', '.join([f"{name}: {price}" for name, price in self.items.items()])
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {{{items_str}}}"
