class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printf = self.head
        while printf is not None:
            print(printf.data)
            printf = printf.next

    def prepend(self, newdata):
        New_Node = Node(newdata)
        New_Node.next = self.head
        self.head = New_Node

    def trans(self):
        print_node = self.head
        while print_node is not None:
            print(print_node.data)
            print_node = print_node.next

    def append(self, New_data):
        New_Node = Node(New_data)
        if self.head is None:
            self.head = New_Node
            return
        last_Node = self.head
        while last_Node.next:
            last_Node = last_Node.next
        last_Node.next = New_Node

    def delete_first(self):
        if self.head is None:
            print("""sorry it is null, you need to insert before deletion
                   can take place.. """)
            return
        self.head = self.head.next


llist = LinkedList()
print("""
      A>Prepend
      B>Append
      c>Delete""")

option = input("ENTER  OPTION:  ")
if option == "a":
    pre_ele = input(' Intsert The Element To Prepend: ')
    llist.prepend(pre_ele)

    while True:
        print(' Do you Want To Perform Any Of The Below Options ? ')
        print("""
        1>Insert Another Node.
        2>Diplay Already Inserted Node.
        3>Deletion.
        """)
        value = input('YOUR OPTION:  ')
        if value == "1":
            pre_ele = input(" Insert the element to prepend:  ")
            llist.prepend(pre_ele)
        elif value == "2":
            llist.listprint()
        elif value == "3":
            llist.delete_first()
            llist.listprint()

if option == "b":
    append_ele = input('Input The Element To Be Append:  ')
    llist.append(append_ele)

    while True:
        print(' Do you Want To Perform Any Of The Below Options? ')
        print("""
        1>Insert Another Node.
        2>Diplay Already Inserted Node.
        3>Deletion.
        """)
        value = input('YOUR OPTION:  ')
        if value == "1":
            append_ele = input('Input The Element To Be Append:  ')
            llist.append(append_ele)
        elif value == "2":
            llist.listprint()
        elif value == "3":
            llist.delete_first()
            llist.listprint()

if option == "c":
    llist.delete_first()
    while True:
        print(' Do you Wish To Insert A Node ? ')
        print("""
        1>YES
        2>Or Perform Deletion
        """)
        value = input('YOUR OPTION:  ')
        if value == "1":
            pre_ele = input(" Insert Into Node:  ")
            llist.prepend(pre_ele)
        elif value == "2":
            llist.delete_first()
            print(" A Node Is Deleted ")
            llist.listprint()


