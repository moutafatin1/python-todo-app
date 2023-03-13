from pathlib import Path
import json


class Todo:
    id: int
    body: str
    completed: bool

    def __init__(self, id: int, body: str, completed: bool = False) -> None:
        self.id = id
        self.body = body
        self.completed = completed

    def print(self):
        print(
            f"{self.id} - TODO: {self.body} - STATUS: {'Completed' if self.completed else 'Ongoing'}"
        )


class TodoApp:
    todos: list[Todo] = []
    data_path = Path("todos.json")

    def __init__(self) -> None:
        data: list = json.loads(self.data_path.read_text())
        for todo in data:
            self.todos.append(Todo(**todo))

    def print_todos(self):
        for todo in self.todos:
            todo.print()
