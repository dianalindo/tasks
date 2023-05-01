def pongestNoReaptString_v1(s):
    start = 0
    max = 0
    charIndex = {}

    for windowEnd in range(len(s)):
        euf