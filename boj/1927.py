import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

class MinHeap:
    def __init__(self):
        self.heap = deque()
        self.size = 0

    def increment_size(self):
        self.size += 1
        return self.size

    def decrement_size(self):
        self.size -= 1
        return self.size

    def parent_idx(self, idx):
        return (idx-1)//2

    def left_child_idx(self, idx):
        return (idx*2)+1
    
    def right_child_idx(self, idx):
        return (idx*2)+2
    
    def has_left_node(self, idx):
        return self.left_child_idx(idx) < self.size
    
    def has_right_node(self, idx):
        return self.right_child_idx(idx) < self.size

    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def push(self, node):
        self.heap.append(node)
        idx = self.increment_size()-1
        if idx >= 1:
            while self.heap[idx] < self.heap[self.parent_idx(idx)]:
                self.swap(idx, self.parent_idx(idx))
                idx = self.parent_idx(idx)
                if idx == 0:
                    break

    def pop(self):
        self.decrement_size()
        popped = self.heap.popleft()
        if self.size > 1:
            self.heap.appendleft(self.heap.pop())
        self.min_heapify(0)
        return popped

    def min_heapify(self, idx):
        if self.has_right_node(idx):
            if self.heap[idx] > self.heap[self.left_child_idx(idx)] or self.heap[idx] > self.heap[self.right_child_idx(idx)]:
                if self.heap[self.left_child_idx(idx)] < self.heap[self.right_child_idx(idx)]:
                    self.swap(idx, self.left_child_idx(idx))
                    self.min_heapify(self.left_child_idx(idx))
                else:
                    self.swap(idx, self.right_child_idx(idx))
                    self.min_heapify(self.right_child_idx(idx))
        elif self.has_left_node(idx):
            if self.heap[idx] > self.heap[self.left_child_idx(idx)]:
                self.swap(idx, self.left_child_idx(idx))
                self.min_heapify(self.left_child_idx(idx))

N = int(input())
minHeap = MinHeap()
for _ in range(N):
    x = int(input())
    if x == 0:
        if minHeap.size>0:
            print(minHeap.pop())
        else:
            print(0)
    else:
        minHeap.push(x)