class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort(reverse = True)
        que= deque()
        for i in deck:
            if que:
                que.appendleft(que.pop())
            que.appendleft(i)
        return que
