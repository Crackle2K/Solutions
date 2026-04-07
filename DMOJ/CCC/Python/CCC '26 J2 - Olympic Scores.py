
s1, s2, s3, s4, s5, difficulty = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
scores = [s1, s2, s3, s4, s5]

highest = max(scores)
lowest = min(scores)
scores.remove(highest)
scores.remove(lowest)

overall = (scores[0] + scores[1] + scores[2]) * difficulty
print(overall)
