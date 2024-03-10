from typing import List, Tuple

_DB = []


def add_task(title: str) -> None:
    _DB.append({"title": title, "completed": False})


def remove_task(index: int) -> None:
    if index >= len(_DB):
        return print('Task does not exist')
    _DB.pop(index)


def mark_task_completed(index: int, completed: bool) -> None:
    if index >= len(_DB):
        return print('Task does not exist')
    _DB[index]["completed"] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    return [(i, task["title"], task["completed"]) for i, task in enumerate(_DB)]


def get_tasks_print() -> str:
    return "\n".join([f"{"✔️ " if task["completed"] else "  "} {i + 1} - {task["title"]}" for i, task in enumerate(_DB)])
