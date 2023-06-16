from collections import defaultdict

class Node:
    def __init__(self,word=None):
        self.word = word
        self.matches = defaultdict(list)