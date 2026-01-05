# for loop

scores = [45, 67, 89, 23]

for score in scores:
    print(score)


# while loop

count = 1

while count <= 5:
    print(count)
    count += 1


# break(Stop the loop)

scores = [45, 67, 89, 23]

for score in scores:
    if score == 89:
        break
    print(score)

# continue (SKIP current loop)

scores = [45, 67, 89, 23]

for score in scores:
    if score < 50:
        continue
    print(score)

# Practice 1: Loop through match scores

match_scores1 = [120, 95, 110, 45, 78]

for score in match_scores1 :
    print("Score", score)


# Practice 2: Filter high scores (≥ 100)

match_scores2 = [120, 95, 110, 45, 78]

for score in match_scores2 :
    if score >= 100:
        print("High Score", score)


# Practice 3: Count high scores

match_scores3 = [120, 95, 110, 45, 78]

count = 0

for score in match_scores3:
    if score >= 100:
        count = count + 1

print("Total high score :", count)




