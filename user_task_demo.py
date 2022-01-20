from user import User
from task import (Task, TaskAssignee)
from redis_om import Migrator

def create_user(name, user_id, job_title):
    user = User(
        name = name, 
        user_id = user_id, 
        job_title = job_title
    ).save()

    print(f"Saved user {user_id} as {user.pk}.")

def create_task(name, task_id, status, description, assignees):
    task_assignees = []

    for assignee in assignees:
        task_assignee = TaskAssignee(
            user_id = assignee
        )

        task_assignees.append(task_assignee)

    task = Task(
        name = name,
        task_id = task_id,
        status = status,
        description = description,
        assigned_to = task_assignees
    ).save()

    print(f"Saved task {task_id} as {task.pk}.")

def show_results(results):
    if not results:
        print("No matches.")
        return

    for result in results:
        print(result)
        print("")

# Create some sample users.
create_user("User 1", "user1", "Janitor")
create_user("User 2", "user2", "Senior Janitor")
create_user("User 3", "user3", "Cleanup Specialist")

# Create some sample tasks.
create_task("Clean room 101", 12, "TODO", "Room 101 needs a good clean.", ["user1", "user2"])
create_task("Drain swimming pool", 19, "IN PROGRESS", "Get all of the water out of the pool.", ["user3"])
create_task("Restock vending machine", 22, "DONE", "Ensure the vending machine is full of various products.", ["user3"])
create_task("Clean room 361", 29, "TODO", "Room 361 is in a terrible state.", ["user1", "user2", "user3"])
create_task("Wipe the gym equipment", 33, "DONE", "Wipe down the treadmills and exercise bikes.", ["user3"])
create_task("Clean room 369", 41, "DONE", "Room 369 has mud on the carpet.", ["user1", "user2", "user3"])
create_task("Clean room 148", 46, "IN PROGRESS", "Room 148 needs the bathroom cleaning.", ["user2", "user3"])

# Create Index
Migrator().run()

# Searches...

print("Users with user_id \"user2\":")
show_results(
    User.find(
        User.user_id == "user2"
    ).all()
)

print("Tasks with a \"TODO\" status")
show_results(
    Task.find(
        Task.status == "TODO"
    ).all()
)

print("Tasks assigned to user with user_id \"user2\":")
show_results(
    Task.find(
        Task.assigned_to.user_id == "user2"
    ).all()
)

print("Tasks assigned to user with user_id \"user2\" with status \"TODO\":")
show_results(
    Task.find(
        (Task.assigned_to.user_id == "user2") &
        (Task.status == "TODO")
    ).all()
)
