class MinHeap():

    def __init__(self):
        self.heap = []

    def extract_min(self):
        popped = self.heap[0]
        last_item = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_item
            self.min_heapify(0)
        return popped


    def is_leaf(self, position):
        return position >= (len(self.heap) // 2) and position <= len(self.heap)

    def min_heapify(self, position):
        if not self.is_leaf(position):
           
            
            left_position = self.left_child(position)
            right_position = self.right_child(position)

            size = len(self.heap)
            smallest = position

            if left_position < size and self.heap[left_position] < self.heap[position]:
                smallest = left_position

            if right_position < size and self.heap[right_position] < self.heap[smallest]:
                smallest = right_position
            
            if smallest != position:
                self.swap(position, smallest)
                self.min_heapify(smallest)


    def insert(self, node):
        
        current = len(self.heap)
        self.heap.append(node)
        
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    

    def swap(self, position1, position2):
        temp = self.heap[position1]
        self.heap[position1] = self.heap[position2]
        self.heap[position2] = temp 


    def right_child(self,position):
        return 2 * position + 2

    def left_child(self,position):
        return 2 * position + 1
    
    def parent(self, position):
        if position == 0: return 0
        return (position - 1) // 2