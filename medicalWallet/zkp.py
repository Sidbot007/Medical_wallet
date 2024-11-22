import random

def zero_knowledge_proof(x, p=11, g=2):
    y = pow(g, x, p)
    r = random.randint(0, p-2)
    h = pow(g, r, p)
    b = random.choice([0, 1])
    s = (r + b * x) % (p - 1)
    left_side = pow(g, s, p)
    right_side = (h * pow(y, b, p)) % p
    return left_side == right_side
