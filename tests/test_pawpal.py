from datetime import datetime
from pawpal_system import Task, Pet, Scheduler


def make_task(name="Test Task", start_hour=8, end_hour=9):
    return Task(
        name=name,
        start_time=datetime(2026, 1, 1, start_hour, 0),
        end_time=datetime(2026, 1, 1, end_hour, 0),
        priority=1,
    )


def test_mark_complete_changes_status():
    task = make_task()
    assert task.is_complete is False
    task.mark_complete()
    assert task.is_complete is True


def test_add_task_increases_task_count():
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler()
    assert pet.task_count == 0
    scheduler.add_task(pet, make_task())
    assert pet.task_count == 1
    scheduler.add_task(pet, make_task())
    assert pet.task_count == 2
