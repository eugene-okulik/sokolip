import random
salary = int(input())
bonus = random.choice([True, False])
additional = random.randint(0, 10000)
if bonus ==True:
    salary_add = salary + additional
else:
    salary_add = salary
print(f"{salary}, {bonus} - '${salary_add}'")
