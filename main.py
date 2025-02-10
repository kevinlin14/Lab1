class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.head = None

    # Checks to see if the current stack is empty
    def isEmpty(self) -> bool:
        return self.head is None

    def peek(self):
        if not self.isEmpty():
            return self.head.value
        return None

    def pop(self):
        if self.isEmpty():
            print("The Stack is Empty")
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def push(self, value):
        # Push the new node onto the stack
        self.head = Node(value, self.head)

    # Display the current state of the stack
    def display(self):
        current = self.head
        if current is None:
            print("Stack is empty")
            return
        
        # Print stack elements
        while current:
            print(f"[ {current.value} ]", end=" -> " if current.next else "")
            current = current.next
        print("")  # Print a newline after displaying the stack

# Kevin 
def file_to_text():
    pass

# Kevin
def determine_type():
    pass

#Pegah
def infix_to_postfix():
    pass

#Pegah
def infix_to_prefix():
    pass

def prefix_to_postfix():
    pass

def prefix_to_infix():
    pass

def postfix_to_prefix():
    pass

# Kevin
def postfix_to_infix():
    pass

# Kevin 
def output():
    pass

def main():
    pass

if __name__ == "__main__":
    main()