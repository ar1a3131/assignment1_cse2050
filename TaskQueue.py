class Task:
    def __init__(self, id, time_left):
        self.id = id
        self.time_left = time_left
        self.next = None
        self.prev = None

    def reduce_time(self,time_per_task):
        self.time_left -= time_per_task
class TaskQueue:
    def __init__(self, time_per_task=1,tasks = []):
        self.current = None
        self.time_per_task = time_per_task
        self.tasks = tasks
    def pop(self):
        self.tasks.pop(0)

    def add_task(self, task):
        if self.current is None:
            self.current = task 
            self.current.next = self.current
            self.current.prev = self.current
        else:
            task.next = self.current   
            task.prev = self.current.prev
            self.current.prev.next = task
            self.current.prev = task
        self.tasks.append(id) 

    def remove_task(self, id):
        if self.current is None:
            raise RuntimeError('id {} not in TaskQueue'.format(id))
        elif self.current.id == id:
            if self.current.next == self.current: 
                self.current = None
            else:
                self.current.prev.next = self.current.next
                self.current.next.prev = self.current.prev
                self.current = self.current.next
            self.tasks.pop() 
        else:
            curr = self.current.next
            while curr != self.current:
                if curr.id == id:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self.pop() 
                    return
                curr = curr.next
                raise RuntimeError('id {} not in TaskQueue'.format(id))

    def __len__(self):
        return len(self.tasks)

    def is_empty(self):
        if self.current is None:
            return True
        else:
            return False

    def execute_tasks(self):
        total_time = 0 
        while not self.is_empty():
            curr = self.current
            for i in range(self.time_per_task):
                if curr.time_left == 0:
                    self.remove_task(curr.id)
                    print("Finished task {} at t= {} seconds".format(curr.id, total_time + i + 1))
                    break 
                else:
                    curr.reduce_time(1)
                    total_time += 1 
            if curr.time_left != 0:
                self.current = self.current.next
        print('Total time = {}'.format(total_time + 1)) 
        return total_time 