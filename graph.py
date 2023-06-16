from graphNode import Node

class Graph:
    def __init__(self,words):
        self.graph = {word:Node(word) for word in words}
        self.createGraph(words)
        
    def createGraph(self,words):
        n = len(words)
        
        for w1 in range(n):
            for w2 in range(n):
                if w1 != w2:
                    self.graph[words[w1]].matches[self.getMatches(words[w1],words[w2])].append(words[w2])
        
    def getMatches(self,word1,word2):
        matches = 0
        for i in range(len(word1)):
            matches += 1 if word1[i] == word2[i] else 0
        
        return matches