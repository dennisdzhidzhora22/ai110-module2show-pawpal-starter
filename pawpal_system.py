import bisect
from dataclasses import dataclass, field
from datetime import datetime, date
from enum import Enum


class Frequency(Enum):
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"


@dataclass
class Task:
    name: str
    start_time: datetime
    end_time: datetime
    priority: int
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
    def add_task(self, pet: Pet, task: Task) -> None:
        """Add a task to a pet's schedule in chronological order."""
        bisect.insort(pet.schedule, task, key=lambda t: t.start_time)
        pet.task_count += 1

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
