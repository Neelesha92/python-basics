tasks = []

def show_menu():
    print('\n To-Do list menu:')
    print('1. Add task')
    print('2. view task')
    print('3. remove task')
    print('4. Mark task as completed')
    print('5. Exit')

def add_task():
    task = input('Enter a new task: ')
    tasks.append({"task":task, "completed":False})
    print(f'your', task, 'has been added.')

def view_task():
    if not tasks:
        print('no task found!')
    else:
        for index, task in enumerate(tasks, start=1):
            status= "completed" if task["completed"] else "pending"
            print(f"{index}. {task['task']} - {status}")

def remove_task():
    view_task()
    task_num = int(input('enter task number to be removed: ')) -1

    if 0<= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f'task', removed_task['task'],' has been removed!')
    else:
        print('invalid task number!')

def mark_task():
    task_num= int(input('enter a task number to mark as completed:')) -1

    if 0<= task_num < len(tasks):
        tasks[task_num]["completed"]= True
        print(f"Task '{tasks[task_num]['task']}' marked as completed!")
    else:
        print('invalid task number')
def main():
    while True:
        show_menu()
        choice = input('Enter your choice: ')

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            print('Goodbye!')
            break
        else:
            print('invalid choice!')

main()