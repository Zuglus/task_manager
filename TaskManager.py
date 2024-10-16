from Task import Task


class TaskManager:
    def __init__(self):
        """Инициализация менеджера задач с пустым списком задач."""
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавляет новую задачу в список."""
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.")

    def mark_task_completed(self, description):
        """Отмечает задачу как выполненную по ее описанию."""
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def list_current_tasks(self):
        """Выводит список текущих (не выполненных) задач."""
        current_tasks = [task for task in self.tasks if not task.is_completed]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            print("Текущие задачи:")
            for task in current_tasks:
                print(task)
