To-Do List with Priorities in Python


This Python script provides a command-line interface for managing your to-do list with priorities. It allows you to:
*Add tasks with optional priority levels (Low, Normal, High).
*View the complete to-do list with priorities and completion status.
*Mark tasks as completed with user confirmation.
*Edit existing tasks (name or priority).


Features:
*Stores tasks in a dictionary with details like task name, completion status, and priority.
*Uses clear and concise function definitions for adding, displaying, marking, and editing tasks.
*Provides user-friendly prompts and messages for interaction.

                                           
Getting Started:
*Save the script as to_do_list.py.
*Run the script from your terminal using python to_do_list.py.
*Follow the interactive menu to manage your tasks.


  
  
  # Define a dictionary to store tasks with more details
tasks = {}

# Function to display the to-do list with priorities
def display_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("To-Do List:")
    for priority, task in tasks.items():
      status = "Done" if task["completed"] else "Not Done"
      print(f"{priority}. {task['task']} ({status}) - {task.get('priority', 'Normal')}")

# Function to add a task with optional priority
def add_task(task_name, priority="Normal"):
  task = {"task": task_name, "completed": False, "priority": priority}
  tasks[len(tasks) + 1] = task  # Use unique key based on task count
  print(f"Task '{task_name}' with priority '{priority}' added.")

# Function to mark a task as completed with user confirmation
def mark_completed(task_number):
  if 1 <= task_number <= len(tasks):
    task = tasks[task_number]
    if not task["completed"]:
      confirmation = input(f"Are you sure you want to mark '{task['task']}' as completed? (y/n): ")
      if confirmation.lower() == 'y':
        task["completed"] = True
        print(f"Task {task_number} marked as completed.")
      else:
        print("Task completion cancelled.")
    else:
      print(f"Task {task_number} is already completed.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Function to edit a task (name or priority)
def edit_task(task_number):
  if 1 <= task_number <= len(tasks):
    task = tasks[task_number]
    print(f"Editing task {task_number}: {task['task']} ({task['completed']}) - {task.get('priority', 'Normal')}")
    choice = input("Edit (n)ame or (p)riority? (n/p): ")
    if choice.lower() == 'n':
      new_name = input("Enter the new task name: ")
      task["task"] = new_name
      print(f"Task name changed to '{new_name}'.")
    elif choice.lower() == 'p':
      new_priority = input("Enter the new priority (Low, Normal, High): ")
      task["priority"] = new_priority.capitalize()
      print(f"Task priority changed to '{new_priority}'.")
    else:
      print("Invalid choice. Please enter 'n' or 'p'.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Main program loop with additional option for editing tasks
while True:
  print("\nOptions:")
  print("1. Display to-do list")
  print("2. Add a task")
  print("3. Mark a task as completed")
  print("4. Remove a task (not implemented yet)")  # Mark for future implementation
  print("5. Edit a task")
  print("6. Quit")
  choice = input("Enter your choice: ")

  if choice == '1':
    display_tasks()
  elif choice == '2':
    task_name = input("Enter the task: ")
    priority = input("Enter priority (Low, Normal, High): ")
    add_task(task_name, priority.capitalize())
  elif choice == '3':
    display_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    mark_completed(task_number)
  elif choice == '4':
    print("Remove task functionality not yet implemented.")  # Placeholder
  elif choice == '5':
    display_tasks()
    task_number = int(input("Enter the task number to edit: "))
    edit_task(task_number)
  elif choice == '6':
    break
  else:
    print("Invalid choice. Please enter a valid option.")
