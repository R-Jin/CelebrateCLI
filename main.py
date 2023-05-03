from typing import List
from pathlib import Path
import datetime

import typer

APP_NAME = "CelebrateCLI"

def prompt_person() -> tuple[str, str, datetime.date]:
    # TODO handle invalid inputs
    # TODO handle duplicate submissions
    first_name = typer.prompt("What's the persons first name").capitalize()
    last_name = typer.prompt("What's the persons last name").capitalize()

    input: str = typer.prompt("Enter the persons birthday in the format YYYY-MM-DD")
    [year, month, day] = map(lambda string : int(string), input.split("-"))

    birthday: datetime.date = datetime.date(year, month, day)

    return (first_name, last_name, birthday)


def add_person(first_name, last_name, birthday):
    print(f"Added {first_name} {last_name} to the reminder list")


def main(show: bool = True, add: bool = False):
    if add:
        (first_name, last_name, birthday) = prompt_person()


if __name__ == "__main__":
    typer.run(main)
