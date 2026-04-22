class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_after(self, target, value):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

    def delete_node(self, value):
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse(node):
            if not node or not node.next:
                return node
            new_head = _reverse(node.next)
            node.next.next = node
            node.next = None
            return new_head

        self.head = _reverse(self.head)

    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beginning(3)
    ll.insert_at_beginning(1)
    ll.insert_at_end(5)
    ll.insert_after(3, 4)

    print("Linked List:")
    ll.display()

    print("Search 4:", ll.search(4))
    print("Middle:", ll.find_middle())

    ll.reverse_iterative()
    print("Reversed:")
    ll.display()

    print("Cycle detected:", ll.detect_cycle())