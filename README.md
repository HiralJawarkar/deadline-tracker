# Student Deadline & Task Manager
A simple Python terminal app to track assignments and deadlines. Built as a course project.

# Why I built this
I kept forgetting assignment deadlines. I'd have 4-5 things due in the same week and only remember the day before. I tried using my phone calendar but setting reminders manually every time was annoying, and I'd still miss things.
So I thought why not just write a small script that shows everything in one place, sorted by what's due first, and screams at me if something's due tomorrow.
That's basically what this is.

# What it does
- Add tasks with a name, deadline and priority
- Shows all pending tasks sorted from nearest to furthest deadline
- Flags anything due within 2 days
- Lets you mark tasks as done or delete them
- When you open it, it immediately tells you if something is overdue or urgent

# How to install and run
- Download this project, just click the green Code button on top of this page and click Download ZIP
- Once downloaded extract the ZIP file and open that folder
- Now open command prompt inside that folder and type python main.py and hit enter
- If it says command not found try python3 main.py

# Instructions for testing
- When the menu opens pick option 1 and add a task, put today's date as the deadline, it should say DUE TODAY
- Add another task but this time put a date that is 1 or 2 days from now, it should say URGENT
- Try adding a task with an old date like something from last month, it should show OVERDUE
- Now go to option 2 and see if all tasks are sorted properly, the nearest deadline should be on top
- Pick option 5 and mark any task as done, then go to option 3 and check that it shows as completed
- Try typing a wrong date like 2026/03/31 instead of 31-03-2026 and see that it shows an error but does not crash
- When done just pick option 7 to exit
