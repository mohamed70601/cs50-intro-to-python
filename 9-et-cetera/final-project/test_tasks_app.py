import project
import csv

project.FILENAME = "test_project.csv"


def test_add_task():
    project.input = lambda _: "Test task"
    project.add_task()

    with open(project.FILENAME) as f:
        rows = list(csv.reader(f))
    assert rows[1] == ["Test task", "False"]


def test_mark_task():
    project.input = lambda _: "1"
    project.mark_task()

    with open(project.FILENAME) as f:
        rows = list(csv.reader(f))
    assert rows[1] == ["Test task", "True"]


def test_remove_task():
    project.input = lambda _: "1"
    project.remove_task()

    with open(project.FILENAME) as f:
        rows = list(csv.reader(f))
    assert len(rows) == 1
