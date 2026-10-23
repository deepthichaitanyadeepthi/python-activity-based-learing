scores = list(map(int, input("Enter student scores: ").split()))

n = int(input("Enter number of groups: "))

groups = [[] for i in range(n)]
totals = [0] * n

scores.sort(reverse=True)

for score in scores:
    i = totals.index(min(totals))
    groups[i].append(score)
    totals[i] += score

for i in range(n):
    print("Group", i + 1, ":", groups[i])
    print("Total score:", totals[i])

print("Difference between group totals:", max(totals) - min(totals))