from collections import deque
from master import Master
from graph import Graph

words = ["acckzz","ccbazz","eiowzz","abcczz"]
guesser = Master(words, 10)
adj = Graph(words)
print('Looking for',guesser.word)

def findWord():
    seen = set()
    for word in words:
        if word in seen: continue
        stack = deque([word])
        seen.add(word)
        while stack:
            curr = stack.pop()
            print(stack,curr)
            matches = guesser.getMatches(word)
            
            if matches == 'Out of Guesses': return False
            elif matches == 'Found': return True
            
            for i in range(matches+1,len(curr)+1):
                for matchingWord in adj.graph[curr].matches[i]:
                    if matchingWord not in seen:
                        stack.append(matchingWord)
                        seen.add(matchingWord)
    
    return False

found = findWord()
print(found)
        


