class Node:
    def __init__(self, data: str, next_node=None):
        self.next_node = next_node
        self.data = data
        self.index = 0

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.count = 1

    def append(self, data):
        node = Node(data)
        if self.firstNode is None:
            self.firstNode = node
            self.lastNode = node
            return

        self.count += 1
        self.lastNode.next_node = node
        prevIndex = self.lastNode.index

        self.lastNode = node
        self.lastNode.index = prevIndex + 1

    def get(self, index: int):
        curNode = self.firstNode
        for _ in range(self.count):
            if index == curNode.index:
                return curNode
            else:
                curNode = curNode.next_node

    def remove(self, index: int):
        if index == 0:
            self.firstNode = self.firstNode.next_node
            return

        prevNode = self.firstNode
        curNode = prevNode.next_node
        for _ in range(1, self.count):
            if index == curNode.index:
                prevNode.next_node = curNode.next_node
            else:
                prevNode = curNode
                curNode = curNode.next_node
        self.count -= 1

    def __str__(self):
        curNode = self.firstNode
        res = ''
        for _ in range(self.count):
            res += str(curNode) + ' '
            curNode = curNode.next_node
        return res


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
