# Queue definition stacks and queues


class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if len(self.stack1) > 0: return self.stack1[-1]
        return None

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0: return None
        t = self.stack1.pop()
        if len(self.stack1) == 0:
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
        return t

    def put(self, value):
        if len(self.stack1) == 0:
            self.stack1.append(value)
        else:
            self.stack2.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

