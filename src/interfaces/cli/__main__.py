import argparse
from src.core.application.services import TodoService
from src.core.infrastructure.in_memory_repository import InMemoryTaskRepository
from src.interfaces.cli.handlers import add_task, list_tasks

def main():
    parser = argparse.ArgumentParser(description="A simple command-line to-do application.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task.")
    add_parser.add_argument("--title", required=True, help="The title of the task.")
    add_parser.add_argument("--description", help="The description of the task.")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks.")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as complete.")
    done_parser.add_argument("--id", type=int, required=True, help="The ID of the task to mark complete.")

    # Undone command
    undone_parser = subparsers.add_parser("undone", help="Mark a task as incomplete.")
    undone_parser.add_argument("--id", type=int, required=True, help="The ID of the task to mark incomplete.")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an existing task.")
    update_parser.add_argument("--id", type=int, required=True, help="The ID of the task to update.")
    update_parser.add_argument("--title", help="New title for the task.")
    update_parser.add_argument("--description", help="New description for the task.")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task.")
    delete_parser.add_argument("--id", type=int, required=True, help="The ID of the task to delete.")

    args = parser.parse_args()

    # Initialize repository and service
    repository = InMemoryTaskRepository()
    service = TodoService(repository)

    if args.command == "add":
        add_task(service, args.title, args.description)
    elif args.command == "list":
        list_tasks(service)
    elif args.command == "done":
        done_task(service, args.id)
    elif args.command == "undone":
        undone_task(service, args.id)
    elif args.command == "update":
        update_task_handler(service, args.id, args.title, args.description)
    elif args.command == "delete":
        delete_task_handler(service, args.id)

if __name__ == "__main__":
    main()
