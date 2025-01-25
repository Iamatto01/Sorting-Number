# Name: Muhammad Saifudin Bin Mohd Jamal
# Matric Number: 2317125
# Section: 2        

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bidirectional_selection_sort_iterative(head):
    if not head or not head.next:
        return head

    start = head
    end = None

    while start != end and start.next != end:
        # Find min and max in the unsorted region
        min_node = start
        max_node = start
        curr = start.next

        while curr != end:
            if curr.data < min_node.data:
                min_node = curr
            if curr.data > max_node.data:
                max_node = curr
            curr = curr.next

        # Swap min_node with start
        if min_node != start:
            start.data, min_node.data = min_node.data, start.data

        # Find the last node in the list if end is None
        if end is None:
            end = get_tail(head)

        # Swap max_node with end
        if max_node != end:
            end.data, max_node.data = max_node.data, end.data

        # Move pointers inward
        start = start.next
        end = get_previous_node(head, end)

    return head

def get_tail(head):
    while head.next:
        head = head.next
    return head

def get_previous_node(head, target):
    prev = None
    while head and head != target:
        prev = head
        head = head.next
    return prev

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create a linked list: 6 -> 3 -> 8 -> 5 -> 2
    head = Node(6)
    head.next = Node(3)
    head.next.next = Node(8)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(2)

    print("Original List:")
    print_list(head)

    head = bidirectional_selection_sort_iterative(head)

    print("Sorted List:")
    print_list(head)
