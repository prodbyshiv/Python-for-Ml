from queue import Queue

q = Queue()

# Sending messages
q.put("Hello")
q.put("How are you?")
q.put("Bye")

# Receiving messages
print(q.get())
print(q.get())
print(q.get())
