# Question 4 - 

# Create a program to implement Stack by using one queue. It allows the user to perform push and pop operations on it.

# Sample -

# What would you like to do? push 3
# What would you like to do? push 5
# What would you like to do? pop
# Popped value:  5
# What would you like to do? pop
# Popped value:  3
# What would you like to do? pop
# Stack is empty.

class Stack:
    def _init_(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if not self.queue:
            print("Stack is empty.")
            return None
        return self.queue.pop(0)