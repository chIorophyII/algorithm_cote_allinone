class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):  # O(n)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, idx):  # O(n)
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    # MY CODE
    # def insert(self, idx, value):
    #     new_node = Node(value)
    #     before = self.head
    #     after = self.head
    #
    #     for _ in range(idx):
    #         if _ < idx-1:
    #             before = before.next
    #         after = after.next

    #     new_node.next = after
    #     before.next = new_node

    def insert(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next  # garbage collector가 알아서 처리해준다.
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            current.next = current.next.next

    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)

ll.insert(0, 9)

print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))
print(ll.get(4))
