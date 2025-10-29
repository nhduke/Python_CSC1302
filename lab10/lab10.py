# lab_stack_queue_short.py


# ---------- PART 1: Stack ----------
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        # TODO: implement push method
        # add the item to the top of the stack
        self._data.append(item)
        

    def pop(self):
        # TODO: implement Error check
        # raise IndexError if stack is empty
        if self.is_empty():
            raise IndexError('Stack is empty')    
           
        # TODO: implement pop method
        # remove and return the top item from the stack
        return self._data.pop()
        

    def is_empty(self):
        # TODO: implement is_empty method
        # return True if stack is empty, False otherwise
        if len(self._data) == 0:
            return True
        else:
            return False


# ---------- PART 2: Queue ----------
class Queue:
    def __init__(self):
        self._data = []
        self._front = 0      # points to the front element

    def enqueue(self, item):
        # TODO: implement enqueue method
        # add the item to the back of the queue
        self._data.append(item)

    def dequeue(self):
        # TODO: implement Error check
        # raise IndexError if queue is empty
        
        if self.is_empty():
            raise IndexError('Queue is empty')
        
        # TODO: implement dequeue operation
        # get the front item and move the front pointer
        
        self._front += 1
        return self._data[self._front - 1]
        

    def is_empty(self):
        # TODO: implement is_empty method
        # return True if queue is empty, False otherwise
        return len(self._data) <= self._front


# ---------- PART 3: Practice ----------



# 1. Push each character of the string onto the stack.
# 2. Pop each character from the stack and append to a new string.
def reverse_string(s: str) -> str:
    """Use Stack to reverse a string."""
    st = Stack()
    for ch in s:
        # TODO: push each character onto the stack
        # use st.push(ch)
        st.push(ch)
    out = ""
    while not st.is_empty():
        # TODO: pop each character from the stack and add to out
        # use st.pop()
        out += st.pop()
    return out

# 1. Enqueue each job in the list.
# 2. Dequeue each job and add to printed_jobs list.
def printer_queue(jobs: list[str]) -> list[str]:
    """
    Simulate printer queue: jobs are printed in arrival order.
    Return a list of printed jobs in the order they were processed.
    """
    q = Queue()
    for job in jobs:
        q.enqueue(job)


    printed_jobs = []
    # TODO: dequeue each job and add to printed_jobs
    
    while not q.is_empty():
        printed_jobs.append(q.dequeue())
        
    return printed_jobs

# ------------------ Quick Tests --------------------
# ---------- DO NOT MODIFY BELOW THIS LINE ----------
def run_tests():
    print("Running quick tests...")
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    jobs = ["Report.pdf", "Invoice.docx", "Graph.png"]
    assert printer_queue(jobs) == jobs

    print("✅ All tests passed!")

if __name__ == "__main__":
    run_tests()
