# Problem Statement
As a college student I noticed that keeping track of multiple assignments and deadlines is harder than it sounds. There is no single place where I can see everything that is due and when. I either forget about an assignment completely or remember it the night before. I wanted to build something simple that solves this problem without needing an internet connection or any app download.

# Scope of the Project
This project is a basic command line program written in Python. It lets you add tasks, view them sorted by deadline, get warned about urgent ones and mark them as done. It runs on your computer locally and stores tasks only for that session, meaning tasks reset when you close the program. It does not connect to the internet, does not send notifications and does not save data to a file. The goal was to keep it simple and focus on the core problem which is knowing what is due and when.

# Target Users
This project is mainly for students who have multiple assignments due across different subjects and want a quick way to see what needs to be done first. It is useful for anyone who prefers using a terminal over installing an app or signing up for something online.

# Features
- Add a task with a name, deadline and priority level
- View all pending tasks sorted from nearest to furthest deadline
- Get a warning when a task is due within 2 days
- See whether a task is on track, coming soon, urgent, due today or overdue
- Mark a task as completed
- Delete a task
- On startup the program immediately shows if anything is overdue or urgent

# Technical Architecture
The whole project is a single Python file called main.py. I kept it in one file because the project is small and splitting it up felt unnecessary for this level.
The program uses a list to store all tasks. Each task is stored as a tuple with four values, the task name, the deadline as a string, the priority and whether it is done or not.

(task_name, deadline, priority, done)
example: ("OS Assignment", "31-03-2026", "High", False)

The datetime module is used to calculate how many days are left until each deadline. Tasks are sorted using Python's built in sort function which compares the deadline dates.
The program is broken into separate functions, one for each feature like adding a task, viewing tasks, marking done and so on. This follows the top down design approach from the course where you break a big problem into smaller parts and solve each one separately.
There is no database or file storage. Everything lives in memory while the program is running.
