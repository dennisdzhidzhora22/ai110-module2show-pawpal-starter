from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    name: str
    start_time: datetime
    end_time: datetime
    priority: int
    description: str = ""


@dataclass
class Pet:
    name: str
    species: str
    schedule: list[Task] = field(default_factory=list)


@dataclass
class Scheduler:
    def add_task(self, pet: Pet, task: Task) -> None:
        pass


@dataclass
class Owner:
    name: str
    scheduler: Scheduler
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def view_schedule(self, pet: Pet, date: str) -> list[Task]:
        pass
