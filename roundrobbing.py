def find(task, time):
    id = [1, 2, 3]
    count = 0
    while task:
        if task[0] <= time:
            print("Task", id[0], "is completed...")
            task.remove(task[0])
            id.remove(id[0])
            count += 1
        else:
            print("Task ", id[0], "is excecuted for ", time, "seconds. Remaining time for task is", task[0] - time)
            task[0] -= time
            task.append(task[0])
            task.remove(task[0])
            id.append(id[0])
            id.remove(id[0])
            count += 1
    print("Total number of runs completed is", count)


task = [10, 5, 8]
time = 4

find(task, time)