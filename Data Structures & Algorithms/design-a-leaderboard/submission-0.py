class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores[playerId] + score if playerId in self.scores else score

    def top(self, K: int) -> int:
        l = list(self.scores.values())
        if not l:
            return 0

        print(l)
        l.sort(reverse=True)
        return sum(l[:K])
        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
