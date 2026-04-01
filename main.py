from pawpal_system import Frequency, Task, Pet, Scheduler, Owner
from datetime import datetime, date

# Create owner
o1 = Owner("Dennis")

# Create two pets
p1 = Pet("Buddy", "Dog")
p2 = Pet("Mittens", "Cat")

# Add two pets
o1.add_pet(p1)
o1.add_pet(p2)

# Create tasks for both pets
t1 = Task(
    name="Feed Buddy",
    start_time=datetime(2025, 6, 1, 8, 0),
    end_time=datetime(2025, 6, 1, 8, 30),
    priority=1,
    description="Feed Buddy his breakfast",
)
t2 = Task(
    name="Walk Buddy",
    start_time=datetime(2025, 6, 1, 9, 0),
    end_time=datetime(2025, 6, 1, 9, 30),
    priority=2,
    description="Take Buddy for a walk",
)
t3 = Task(
    name="Play with Buddy",
    start_time=datetime(2025, 6, 1, 10, 0),
    end_time=datetime(2025, 6, 1, 10, 30),
    priority=3
)

t4 = Task(
    name="Feed Mittens",
    start_time=datetime(2025, 6, 1, 7, 0),
    end_time=datetime(2025, 6, 1, 7, 30),
    priority=1,
    description="Feed Mittens her breakfast"
)
t5 = Task(
    name="Clean up after Mittens",
    start_time=datetime(2025, 6, 1, 8, 0),
    end_time=datetime(2025, 6, 1, 8, 15),
    priority=2,
    description="Clean Mittens' litterbox"
)
t6 = Task(
    name="Play with Mittens",
    start_time=datetime(2025, 6, 1, 10, 30),
    end_time=datetime(2025, 6, 1, 11, 0),
    priority=3
)

# Add tasks for both pets
o1.scheduler.add_task(p1, t1)
o1.scheduler.add_task(p1, t2)
o1.scheduler.add_task(p1, t3)
o1.scheduler.add_task(p2, t4)
o1.scheduler.add_task(p2, t5)
o1.scheduler.add_task(p2, t6)

print("Today's Schedule")
print("-" * 40)
for task in o1.scheduler.view_schedule(o1.pets, date(2025, 6, 1)):
    start = task.start_time.strftime("%I:%M %p")
    end = task.end_time.strftime("%I:%M %p")
    status = "X" if task.is_complete else "O"
    print(f"{status} [{start} - {end}] {task.name} (Priority: {task.priority})")
    if task.description:
        print(f"   {task.description}")