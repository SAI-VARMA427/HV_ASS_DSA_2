# Question 3 - 

# Create a program on Stack that will have the following operations - 

# Minimum - This function will find out the minimum element among all the elements that are inserted in the stack.
# Top - This function will find out the top element in the stack. It should show the updated top element, even if we perform the “push” or “pop” operations.
# Push - This function will insert new elements in the stack. The elements need to be inserted one above the other. 
# Pop - This function will delete the elements from the stack. The last inserted element needs to be popped from the stack. 

# We can create different functions for the above operations.


class Stack:
    def _init_(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def minimum(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]