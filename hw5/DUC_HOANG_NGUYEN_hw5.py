import tkinter as tk
from tkinter import messagebox

class LinkedListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

    def createLoopedList(self, *inputs):
        self.val = inputs[0]
        current = self
        for num in inputs[1:]:
            current.next = LinkedListNode(num)
            current = current.next
        current.next = self
        return self

class PotatoGameGUI:
    def __init__(self, root):
        self.root = root
        
        root.title("Potato Game")
        
        #inputs
        tk.Label(root, text="Enter number of player N: (1 < N < 12):").grid(row=0, column=0, sticky="w")
        self.entryN = tk.Entry(root, width=5)
        self.entryN.grid(row=0, column=1)
        
        tk.Label(root, text="Enter steps K: (K ≥ 1):").grid(row=1, column=0, sticky="w")
        self.entryK = tk.Entry(root, width=5)
        self.entryK.grid(row=1, column=1)
        
        #start
        self.startButton = tk.Button(root, text="Start", command=self.startGame)
        self.startButton.grid(row=2, column=0, columnspan=2)
        
        #log message box
        tk.Label(root, text="Game Messages:").grid(row=3, column=0, columnspan=2)
        self.logBox = tk.Text(root, height=10, width=40, state="disabled")
        self.logBox.grid(row=4, column=0, columnspan=2)
        
        #canvas to show player
        self.canvas = tk.Canvas(root, width=400, height=250, bg="white")
        self.canvas.grid(row=5, column=0, columnspan=2, pady=5)
        
        #elimiate button is not shown at the start
        self.eliminateButton = None
        
        #preset some key value
        self.head = None
        self.K = 1
        self.current = None
        self.prev = None
        self.playerIcon = {}

    #logging message function
    def log(self, msg):
        self.logBox.config(state="normal")
        self.logBox.insert(tk.END, msg + "\n")
        self.logBox.see(tk.END)
        self.logBox.config(state="disabled")

    #reset UI after a game
    def reset_ui(self): 
        self.canvas.delete("all")
        
        if self.eliminateButton:
            self.eliminateButton.destroy()
            self.eliminateButton = None
            
        self.logBox.config(state="normal")
        self.logBox.delete(1.0, tk.END)
        self.logBox.config(state="disabled")
        
        self.playerIcon.clear()
    
        self.head = None
        self.current = None
        self.prev = None

    def startGame(self):
        self.reset_ui()
        try:
            N = int(self.entryN.get())
            self.K = int(self.entryK.get())
        except:
            messagebox.showinfo("Invalid Input", "Please enter N and K value.")
            return
        if not (1 < N < 12):
            messagebox.showinfo("Invalid Input", "Invalid N: 1 < N < 12")
            return
        if self.K < 1:
            messagebox.showinfo("Invalid Input", "Invalid K : K ≥ 1")
            return
        
        self.head = LinkedListNode()
        self.head.createLoopedList(*list(range(0, N))) #create a looped list
        
        #record the first player and last player 
        self.current = self.head
        self.prev = self.head
        while self.prev.next != self.head:
            self.prev = self.prev.next
        
        #draw the players    
        self.drawPlayers()
        
        #show elimiate button
        self.eliminateButton = tk.Button(self.root, text="Eliminate", command=self.eliminateStep)
        self.eliminateButton.grid(row=6, column=0, columnspan=2, pady=8)
        
        self.log(f"Game started. N={N}, K={self.K}")

    def drawPlayers(self):
        self.canvas.delete("all")
        self.playerIcon.clear()

        if self.current is None:
            return

        start_x = 30
        current = self.current
        seen = set() #only print the not shown nodes
        index = 0

        while current.val not in seen:
            seen.add(current.val)
            x = start_x + index * 35
            txt = self.canvas.create_text(x, 120, text=str(current.val), font=("Arial", 16))
            self.playerIcon[current.val] = txt
            index += 1
            current = current.next


    def countPlayers(self): #count remaining player
        if self.current is None:
            return 0
        count = 1
        node = self.current
        while node.next != self.current:
            count += 1
            node = node.next
        return count
    
    def eliminateStep(self):
        if self.current is None:
            return

        #move k-1 steps to the to be deleted node
        for _ in range(self.K - 1):
            self.prev = self.current
            self.current = self.current.next

        eliminatedPlayer = self.current.val
        self.prev.next = self.current.next
        self.current = self.prev.next

        if eliminatedPlayer in self.playerIcon:
            self.canvas.delete(self.playerIcon[eliminatedPlayer])
            del self.playerIcon[eliminatedPlayer]

        self.log(f"Player {eliminatedPlayer} eliminated.")

        if self.countPlayers() == 1:
            winner = self.current.val
            messagebox.showinfo("Notification", f"Winner is player {winner}")
            self.reset_ui()
            return

        self.drawPlayers()


root = tk.Tk()
app = PotatoGameGUI(root)
root.mainloop()
