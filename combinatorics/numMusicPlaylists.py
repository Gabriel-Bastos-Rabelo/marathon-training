class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = {}
        def count(cur_goal, old_songs):

            if cur_goal == 0 and old_songs == n:
                
                return 1
            if cur_goal == 0 or old_songs > n:
                return 0

            if (cur_goal, old_songs) in dp:
                return dp[(cur_goal, old_songs)]

            #escolhendo uma nova musica
            res = (n - old_songs) * count(cur_goal - 1, old_songs + 1)
            
            if old_songs > k:
                res += (old_songs - k) * count(cur_goal - 1, old_songs)

            dp[(cur_goal, old_songs)] = res % (10 ** 9 + 7)
            return res % (10 ** 9 + 7)
        return count(goal, 0)