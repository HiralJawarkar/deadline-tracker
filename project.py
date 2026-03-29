import datetime

tasks = []

while True:
    print("\n1. add task")
    print("2. view tasks")
    print("3. mark task done")
    print("4. exit")

    choice = input("enter choice: ")

    if choice == "1":
        name = input("task name: ")
        deadline = input("deadline (DD-MM-YYYY): ")
        priority = input("priority (high/medium/low): ")

        # storing as tuple, learned this in class
        task = (name, deadline, priority, False)
        tasks.append(task)
        print("task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("no tasks yet")
        else:
            print("\nyour tasks:")
            for i in range(len(tasks)):
                t = tasks[i]

                # calculate days left
                try:
                    d = datetime.datetime.strptime(t[1], "%d-%m-%Y").date()
                    today = datetime.date.today()
                    days = (d - today).days

                    if days < 0:
                        status = "OVERDUE"
                    elif days == 0:
                        status = "due today"
                    elif days <= 2:
                        status = "urgent"
                    else:
                        status = str(days) + " days left"
                except:
                    status = "invalid date"

                if t[3] == True:
                    status = "done"

                print(str(i+1) + ". " + t[0] + " | " + t[1] + " | " + t[2] + " | " + status)

    elif choice == "3":
        if len(tasks) == 0:
            print("no tasks")
        else:
            num = int(input("enter task number to mark done: ")) - 1
            t = tasks[num]
            tasks[num] = (t[0], t[1], t[2], True)
            print("marked as done")

    elif choice == "4":
        print("bye")
        break

    else:
        print("invalid choice")
