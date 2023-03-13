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

    def new_todo(self):
        body = input("Add new todo: ")
        todo = Todo(len(self.todos) + 1, body)
        self.todos.append(todo)
        self.save()

        print("Todo created Successfully!")

    def delete_todo(self):
        todo_id = int(input("Please insert the ID of the todo you want to delete:"))
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        self.save()

    def save(self):
        self.data_path.write_text(json.dumps([todo.__dict__ for todo in self.todos]))
