class Task:
    def __init__(self, description, deadline):
        """
        Инициализация новой задачи.

        :param description: Описание задачи.
        :param deadline: Срок выполнения задачи (например, в формате 'YYYY-MM-DD').
        """
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_completed(self):
        """Отмечает задачу как выполненную."""
        self.is_completed = True

    def __str__(self):
        status = 'Выполнено' if self.is_completed else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"
