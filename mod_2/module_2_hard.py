import random


def puzzle():
    a = random.randint(3, 20)
    b = []
    for i in range(1, a):
        for j in range(i + 1, a):
            if a % (i + j) == 0:
                b.append(f"{i}{j}")

    print(a, "-", ''.join(b))


puzzle()
