class LinkedListTail:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def size(self):
        return self.count

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def add_to_head(self, item):
        new_node = Node(item, self.head)
        if self.is_empty():
            self.tail = new_node
        self.head = new_node
        self.count += 1

    def add_to_tail(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def remove_from_head(self):
        if not self.is_empty():
            self.head = self.head.next
            self.count -= 1
            if self.count == 0:
                self.tail = None

    def remove_from_tail(self):
        if not self.is_empty():
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.count -= 1
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
                self.count -= 1

    def __str__(self):
        if self.is_empty():
            return "Empty list"

        result = "Head -->"
        current = self.head
        while current is not None:
            result += " " + str(current.data) + " -->"
            current = current.next
        result = result[:-4] + " <-- Tail"
        return result
