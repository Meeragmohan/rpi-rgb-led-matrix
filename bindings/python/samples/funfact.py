import random


def get_random_fact(basepath):
    with open(basepath+'/facts/facts.txt', 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()

#print(get_random_fact('.'))