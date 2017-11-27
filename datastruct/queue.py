from collections import deque

list=[1,2,3,4]
queue=deque(list)
queue.append(5)
print(queue)
queue.popleft()
print(queue)