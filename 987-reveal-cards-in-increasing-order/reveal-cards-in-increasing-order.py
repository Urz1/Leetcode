class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort()
        ans = [0] * len(deck)
        queue.extend([i for i in range(len(deck))])
        i = 0
        while len(queue) >= 2:
            temp = queue.popleft()
            ans[temp] = deck[i]
            queue.append(queue.popleft())
            i+=1
        temp = queue.pop()
        ans[temp] = deck[i]
        return ans