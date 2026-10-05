# tasks.py
tasks = []

def add_task(title, priority="medium"):
    tasks.append({"title": title, "priority": priority, "done": False})
    print(f"Added: {title} ({priority})")

def list_tasks():
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "⬜"
        print(f"{i}. {status} {t['title']} [{t['priority']}]")

add_task("Write report", "high")
add_task("Clean inbox")
list_tasks()
