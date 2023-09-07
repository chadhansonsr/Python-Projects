class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f' value is {self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_node(self, value):
        node = Node(value, self.head)
        self.head = node
        self.length = 1


def display_list(list):
    temp = list
    while temp:
        print(temp.value, end="  ")
        temp = temp.next
    print("")


def check_list(list, value):
    temp = list
    while temp:
        if temp.value == value:
            return True
        temp = temp.next
    return False


def union(list1, list2):
    dict = {}
    union = LinkedList()
    temp = list1
    while temp:
        union.insert_node(temp.value)
        dict[temp.value] = 1
        temp = temp.next

    temp = list2
    while temp:
        if (dict.get(temp.value, None) is None):
            union.insert_node(temp.value)
        temp = temp.next
    return union.head


def intersection(list1, list2):
    dict = {}
    intersection = LinkedList()
    temp = list1
    while temp:
        dict[temp.value] = 1
        temp = temp.next

    temp = list2
    while temp:
        if dict.get(temp.value, None):
            intersection.insert_node(temp.value)
        temp = temp.next
    return intersection.head


list1 = LinkedList()
list1.insert_node(3)
list1.insert_node(31)
list1.insert_node(2)
list1.insert_node(35)
list1.insert_node(6)
list1.insert_node(655)
list1.insert_node("str")
list1.insert_node(True)
list1.insert_node(1)
list1.insert_node(21)
print("Linked list 1: ")
display_list(list1.head)  

list2 = LinkedList()
list2.insert_node(5)
list2.insert_node(3)
list2.insert_node(4)
list2.insert_node(9)
list2.insert_node(60)
list2.insert_node(1)
list2.insert_node(11)
list2.insert_node(21)
list2.insert_node(11111111111)
print("Linked list 2: ")
display_list(list2.head)

union1 = union(list1.head, list2.head)
print("\n\nThe union of lists 1 and 2 is: ")
display_list(union1)
# prints 5 4 9 60 11 11111111111 3 31 2 35 6 655 str True 1 21

intersection1 = intersection(list1.head, list2.head)
print("The intersection of lists 1 and 2 is: ")
display_list(intersection1)
# prints 3 1 21

list3 = LinkedList()
list3.insert_node(5)
list3.insert_node(6)
list3.insert_node(7)
list3.insert_node(8)
list3.insert_node(9)
list3.insert_node(10)
print("\n\nLinked list 3: ")
display_list(list3.head)

list4 = LinkedList()
list4.insert_node(0)
list4.insert_node(1)
list4.insert_node(2)
list4.insert_node(3)
list4.insert_node(4)
print("Linked list 4: ")
display_list(list4.head)

union2 = union(list3.head, list4.head)
print("\n\nThe union of lists 3 and 4 is: ")
display_list(union2)
# prints 0 1 2 3 4 5 6 7 8 9 10

intersection2 = intersection(list3.head, list4.head)
print("The intersection of lists 3 and 4 is: ")
display_list(intersection2)
# prints a blank line since there's no interesetion of values

list5 = LinkedList()
list5.insert_node("B")
list5.insert_node("L")
list5.insert_node("U")
list5.insert_node("E")
list5.insert_node("!")
list5.insert_node("!")
list5.insert_node("!")
list5.insert_node(" ")
list5.insert_node(" ")
print("\n\nLinked list 5: ")
display_list(list5.head)

list6 = LinkedList()
list6.insert_node("G")
list6.insert_node("O")
print("Linked list 6: ")
display_list(list6.head)

union3 = union(list5.head, list6.head)
print("\n\nThe union of lists 5 and 6 is: ")
display_list(union3)
# prints GOBLUE!!! with two spaces at the end

intersection3 = intersection(list5.head, list6.head)
print("The intersection of lists 5 and 6 is: ")
display_list(intersection3)
# prints a blank line since there's no interesetion of values
