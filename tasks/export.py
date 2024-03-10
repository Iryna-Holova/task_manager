from typing import List, Tuple
import os
from openpyxl import Workbook


def save_to_file(tasks: List[Tuple[int, str, bool]], file_name: str) -> None:
    directory = "./out/"

    if not os.path.exists(directory):
        os.makedirs(directory)

    wb = Workbook()
    ws = wb.active

    ws.append(["Index", "Title", "Completed"])

    for task in tasks:
        ws.append(task)

    wb.save(f"{directory}{file_name}.xlsx")
