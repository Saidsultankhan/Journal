name_and_scores = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    name_and_scores.append([name, score])
    scores.append(score)
scores_result = list(set(sorted(scores)))

result = []
for i in range(len(name_and_scores)):
    if scores_result[1] == name_and_scores[i][1]:
        result.append(name_and_scores[i][0])
for i in sorted(result):
    print(i)
