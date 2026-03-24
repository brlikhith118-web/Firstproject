# app.py

print("Welcome to Task Manager App 🚀")

def greet_user(name):
    return f"Hello, {name}! Welcome to the app."


# 🔐 Login Feature
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful ✅"
    return "Invalid Credentials ❌"


if __name__ == "__main__":
    print(greet_user("User"))
    print(login("admin", "1234"))
