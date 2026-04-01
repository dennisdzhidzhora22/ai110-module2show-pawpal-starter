# PawPal+ Project Reflection

## 1. System Design

Three core actions users should be able to perform:
- Add a pet
- Add a task for a pet to the schedule
- See today's scheduled tasks for a pet

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design consisted of an Owner, Pet, Task, and Scheduler class. An Owner holds a list of Pet objects, can add a pet, and holds a Scheduler object it can call to work on a pet's schedule. Pets hold a list of Tasks. Tasks hold a start time, end time, frequency, completion status, and priority. A Scheduler schedules a task in a pet's schedule, and can return all tasks for a pet for a certain day.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I ended up making two changes. The first change was to change the Owner class to create a Scheduler as a default value for the scheduler parameter. This simplifies the syntax, as without it, users would have to pass in a scheduler every time a new Owner was made, like `owner = Owner("Alice", Scheduler())`. The second change was to change the type of the date parameter in the `Owner.view_schedule()` function from a str to a date object. This change lets the date be directly compared against the start times of tasks, removing the overhead of string parsing.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
