from TaskQueue import Task, TaskQueue

t1 = Task(id=1, time_left=3)
t2 = Task(id=2, time_left=5)
t3 = Task(id=3, time_left=8)
tasklist = [t1,t1,t3]
TQ = TaskQueue(time_per_task=1)

for task in tasklist:
    TQ.add_task(task)

TQ.remove_task(1)

assert (TQ.__len__() == 2)
print("TaskQueue length: " + str(TQ.__len__()))
assert (TQ.is_empty() == False)
TQ.execute_tasks()
assert (TQ.is_empty() == True)





