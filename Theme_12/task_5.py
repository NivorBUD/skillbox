class Stack:
    def __init__(self):
        self.data = []

    def add(self, element):
        self.data.append(element)

    def pop(self):
        self.data.remove(len(self.data))

    def __str__(self):
        return ', '.join([str(i) for i in self.data])


class TaskManager:
    def __init__(self):
        self.data = {}

    def new_task(self, task: str, priority: int):
        if priority not in self.data.keys():
            self.data[priority] = Stack()
        self.data[priority].add(task)

    def __str__(self):
        res = '\n'.join(['{} - {}'.format(priority, self.data[priority])
                         for priority in sorted(self.data.keys())])
        return res


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)


print('\nПроверка стека')
stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
stack.add(4)

print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
