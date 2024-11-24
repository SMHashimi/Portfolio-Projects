first_name = input("First Name: ").lower()
second_name = input("Second Name: ").lower()

def calculate_love_score(name1, name2):
    t = 0
    r = 0
    u = 0
    e = 0
    l = 0
    o = 0
    v = 0
    e_in_love = 0

    for letter in name1:
        if letter == "t":
            t += 1
        if letter == "r":
            r += 1
        if letter == "u":
            u += 1
        if letter == "e":
            e += 1

    for letter in name2:
        if letter == "t":
            t += 1
        if letter == "r":
            r += 1
        if letter == "u":
            u += 1
        if letter == "e":
            e += 1

    for letter in name1:
        if letter == "l":
            l += 1
        if letter == "o":
            o += 1
        if letter == "v":
            v += 1
        if letter == "e":
            e_in_love += 1

    for letter in name2:
        if letter == "l":
            l += 1
        if letter == "o":
            o += 1
        if letter == "v":
            v += 1
        if letter == "e":
            e_in_love += 1

    print(f"T occurs {t} times")
    print(f"R occurs {r} times")
    print(f"U occurs {u} times")
    print(f"E occurs {e} times")
    print(f"L occurs {l} times")
    print(f"O occurs {o} times")
    print(f"V occurs {v} times")
    print(f"E occurs {e} times")

    # print(f"Total = {t + r + u + e}")
    # print(f"Total = {l + o + v + e}")
    total = str(t + r + u + e) + str(l + o + v + e)
    print(f"Love score = {total}")

calculate_love_score(first_name, second_name)







