class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull_cnt = sum([a == b for a , b in zip(secret, guess)])
        secret_freq = collections.Counter(secret)
        union_cnt = 0
        for i in range(len(guess)):
            if guess[i] in secret_freq and secret_freq[guess[i]] > 0:
                union_cnt += 1
                secret_freq[guess[i]] -= 1
        return '%sA%sB' % (bull_cnt, union_cnt - bull_cnt)
