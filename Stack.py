class Node():
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack():
    def __init__(self):
        self.top = Node(None)
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size = self.size + 1

    def pop(self):
        if self.size > 0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node.data
        raise IndexError("the stack is empty")

    def peek(self):
        if self.size > 0:
            return self.top.data
        raise IndexError("the stack is empty")

    def __repr__(self) -> str:
        r = ""
        node = self.top
        while (node.data):
            r = r + str(node.data) + "\n"
            node = node.next
        return r


stack = Stack()

stack.push(123)
stack.push("Eli")
stack.push("Alcatel")
stack.push("Alcalina")

print(stack)
print("Topo da pilha: "+stack.peek())


print("Removendo: "+stack.pop() + "\n")

print(stack)
print("Topo da pilha: "+stack.peek())
