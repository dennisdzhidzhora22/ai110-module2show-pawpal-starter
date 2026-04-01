from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Scheduler, Priority, Frequency


def make_task(name="Test Task", start_hour=8, end_hour=9, frequency=Frequency.ONCE):
    return Task(
        name=name,
        start_time=datetime(2026, 1, 1, start_hour, 0),
        end_time=datetime(2026, 1, 1, end_hour, 0),
        priority=Priority.MEDIUM,
        frequency=frequency,
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
    scheduler.add_task(pet, make_task(start_hour=8, end_hour=9))
    assert pet.task_count == 1
    scheduler.add_task(pet, make_task(start_hour=10, end_hour=11))
    assert pet.task_count == 2


def test_sort_by_time_returns_chronological_order():
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler()
    scheduler.add_task(pet, make_task(name="Late task", start_hour=10, end_hour=11))
    scheduler.add_task(pet, make_task(name="Early task", start_hour=7, end_hour=8))
    scheduler.add_task(pet, make_task(name="Middle task", start_hour=8, end_hour=9))
    sorted_tasks = scheduler.sort_by_time(pet)
    start_times = [t.start_time for t in sorted_tasks]
    assert start_times == sorted(start_times)


def test_complete_daily_task_creates_next_day_task():
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler()
    task = make_task(frequency=Frequency.DAILY)
    scheduler.add_task(pet, task)
    scheduler.complete_task(pet, task)
    assert task.is_complete is True
    assert pet.task_count == 2
    next_task = pet.schedule[1]
    assert next_task.start_time == task.start_time + timedelta(days=1)
    assert next_task.is_complete is False


def test_back_to_back_tasks_are_not_a_conflict():
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler()
    scheduler.add_task(pet, make_task(name="First task", start_hour=8, end_hour=9))
    scheduler.add_task(pet, make_task(name="Second task", start_hour=9, end_hour=10))
    assert pet.task_count == 2


def test_recurring_task_into_conflict_is_not_rescheduled(capsys):
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler()
    daily_task = make_task(name="Morning walk", start_hour=8, end_hour=9, frequency=Frequency.DAILY)
    blocking_task = Task(
        name="Vet appointment",
        start_time=datetime(2026, 1, 2, 8, 0),
        end_time=datetime(2026, 1, 2, 9, 0),
        priority=Priority.HIGH,
    )
    scheduler.add_task(pet, daily_task)
    scheduler.add_task(pet, blocking_task)
    scheduler.complete_task(pet, daily_task)
    assert pet.task_count == 2
    output = capsys.readouterr().out
    assert "Warning" in output


def test_conflicting_task_is_rejected(capsys):
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler()
    scheduler.add_task(pet, make_task(name="First task", start_hour=8, end_hour=9))
    scheduler.add_task(pet, make_task(name="Conflicting task", start_hour=8, end_hour=9))
    assert pet.task_count == 1
    output = capsys.readouterr().out
    assert "Warning" in output
    assert "Conflicting task" in output
