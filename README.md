# app.py

print("Welcome to Task Manager App 🚀")

def greet_user(name):
    return f"Hello, {name}! Welcome to the app."


# 🔐 Login Feature
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful ✅"
    return "Invalid Credentials ❌"


# 📋 Task Feature
tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added!"

def view_tasks():
    return tasks


# 🔔 Notification Feature
def send_notification(message):
    return f"Notification sent: {message}"


if __name__ == "__main__":
    print(greet_user("User"))
    print(login("admin", "1234"))
    print(add_task("Learn Git"))
    print(view_tasks())
    print(send_notification("Task Completed!"))
