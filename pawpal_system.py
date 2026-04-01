from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from enum import Enum


class Frequency(Enum):
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    name: str
    start_time: datetime
    end_time: datetime
    priority: Priority
    description: str = ""
    frequency: Frequency = Frequency.ONCE
    is_complete: bool = False

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.is_complete = True


@dataclass
class Pet:
    name: str
    species: str
    schedule: list[Task] = field(default_factory=list)
    task_count: int = 0


@dataclass
class Scheduler:
    def _conflicts(self, schedule: list[Task], task: Task) -> Task | None:
        """Return the first task in the schedule that overlaps with the given task, or None."""
        return next(
            (t for t in schedule if task.start_time < t.end_time and task.end_time > t.start_time),
            None
        )

    def add_task(self, pet: Pet, task: Task) -> None:
        """Add a task to a pet's schedule, printing a warning and skipping if it conflicts with an existing task."""
        conflicting = self._conflicts(pet.schedule, task)
        if conflicting:
            print(
                f"Warning: '{task.name}' conflicts with '{conflicting.name}' "
                f"({conflicting.start_time:%I:%M %p} - {conflicting.end_time:%I:%M %p})"
            )
            return
        pet.schedule.append(task)
        pet.task_count += 1

    def sort_by_time(self, pet: Pet) -> list[Task]:
        """Return a pet's schedule sorted by start time."""
        return sorted(pet.schedule, key=lambda t: t.start_time)

    def complete_task(self, pet: Pet, task: Task) -> None:
        """Mark a task complete and schedule the next occurrence if recurring."""
        task.mark_complete()
        if task.frequency == Frequency.ONCE:
            return
        delta = timedelta(days=1) if task.frequency == Frequency.DAILY else timedelta(weeks=1)
        next_task = Task(
            name=task.name,
            start_time=task.start_time + delta,
            end_time=task.end_time + delta,
            priority=task.priority,
            description=task.description,
            frequency=task.frequency,
        )
        self.add_task(pet, next_task)

    def filter_by_status(self, pet: Pet, is_complete: bool) -> list[Task]:
        """Return tasks from a pet's schedule filtered by completion status."""
        return [t for t in pet.schedule if t.is_complete == is_complete]

    def view_schedule(self, pets: Pet | list[Pet], date: date) -> list[Task]:
        """Return all tasks for one or more pets on a given date, sorted by start time."""
        if isinstance(pets, Pet):
            pets = [pets]
        tasks = [t for pet in pets for t in pet.schedule if t.start_time.date() == date]
        return sorted(tasks, key=lambda t: t.start_time)


@dataclass
class Owner:
    name: str
    scheduler: Scheduler = field(default_factory=Scheduler)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)
