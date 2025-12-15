from fastapi import FastAPI
import json
import uvicorn


app = FastAPI(
    title="Todo API",
    description="A simple Todo API using FastAPI and JSON file storage",
    version="1.0.0"
)

class Todo:

    file_path = 'todo.json'

    def load_json(self, file_path: str):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def save_json(self, file_path: str, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True

    def get_all_todos(self):
        return self.load_json(self.file_path)

    def add_todo(self, todo_item: str):
        todos = self.load_json(self.file_path)
        todos.append({"item": todo_item, "completed": False})
        self.save_json(self.file_path, todos)
        return todos

    def mark_todo_completed(self, index: int):
        todos = self.load_json(self.file_path)
        if 0 <= index < len(todos):
            todos[index]['completed'] = True
            self.save_json(self.file_path, todos)
            return todos
        else:
            return {"error": "Index out of range"}

    def delete_todo(self, index: int):
        todos = self.load_json(self.file_path)
        if 0 <= index < len(todos):
            todos.pop(index)
            self.save_json(self.file_path, todos)
            return todos
        else:
            return {"error": "Index out of range"}

    def update_todo(self, index: int, new_item: str):
        todos = self.load_json(self.file_path)
        if 0 <= index < len(todos):
            todos[index]['item'] = new_item
            self.save_json(self.file_path, todos)
            return todos
        else:
            return {"error": "Index out of range"}                

@app.get("/todos")
def get_todos():
    todo = Todo()
    return todo.get_all_todos()


@app.post("/add_todo")
def add_todo_item(item: str):
    todo = Todo()
    return todo.add_todo(item)


@app.post("/complete_todo/{index}")
def complete_todo_item(index: int):
    todo = Todo()
    return todo.mark_todo_completed(index)


@app.delete("/delete_todo/{index}")
def delete_todo_item(index: int):
    todo = Todo()
    return todo.delete_todo(index)


@app.put("/update_todo/{index}")
def update_todo_item(index: int, new_item: str):
    todo = Todo()
    return todo.update_todo(index, new_item)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)