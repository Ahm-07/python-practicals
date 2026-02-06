print("UIN:251A025")
print("Date:03-02-2026")
# Task List Manager (Simple Version)
print("\n---Task List Manager---")
# Create a task list
tasks = ["Wakeup", "Brush", "Breakfast"]
# Display tasks
print("\nCurrent Tasks:")
for task in tasks:
    print(task)
# Add a new task
new_task = input("\nEnter a new task to add: ")
tasks.append(new_task)
print("\nTasks after adding:")
for task in tasks:
    print(task)
# Remove a task
remove_task = input("\nEnter a task name to remove: ")
if remove_task in tasks:
    tasks.remove(remove_task)
else:
    print("Task not found")
print("\nTasks after removing:")
for task in tasks:
    print(task)
# Update a task
old_task = input("\nEnter task name to update: ")
if old_task in tasks:
    index = tasks.index(old_task)
    new_value = input("Enter new task name: ")
    tasks[index] = new_value
else:
    print("Task not found")
print("\nTasks after updating:")
for task in tasks:
    print(task)
# Sort tasks
tasks.sort()
print("\nTasks after sorting:")
for task in tasks:
    print(task)
# Convert list to tuple
task_tuple = tuple(tasks)
print("\nTasks stored in tuple:")
for task in task_tuple:
    print(task)
