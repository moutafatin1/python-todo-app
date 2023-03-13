from todoapp import TodoApp

prompt = "\nWelcome to the ultimate Todo Application\n"
prompt += "[0] - To leave the app\n"
prompt += "[1] - See all todos\n"
prompt += "[2] - Add new todo\n"
prompt += "[3] - Delete a todo\n"
prompt += ": "

app = TodoApp()


choice = int(input(prompt))
while True:
    if choice == 0:
        break

    if choice == 1:
        app.print_todos()

    if choice == 2:
        app.new_todo()

    if choice == 3:
        app.delete_todo()

    choice = int(input("new command: "))
