from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        digits = []
        for digit in str(n):
            digits.append(int(digit))

        score = 0
        counts = Counter(digits)
        for count in counts:
            score += (count * counts[count])
        return score
