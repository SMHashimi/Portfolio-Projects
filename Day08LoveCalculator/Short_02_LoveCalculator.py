first_name = input("First Name: ")
second_name = input("Second Name: ")
combined_name = first_name + " " + second_name

def calculate_love_score(name1, name2):
    t = 0
    r = 0
    u = 0
    e = 0
    l = 0
    o = 0
    v = 0
    e_in_love = 0

    for letter in combined_name:
        if letter == "t":
            t += 1
        if letter == "r":
            r += 1
        if letter == "u":
            u += 1
        if letter == "e":
            e += 1
        if letter == "l":
            l += 1
        if letter == "o":
            o += 1
        if letter == "v":
            v += 1
        if letter == "e":
            e_in_love += 1

    print(f"T occurs {t} times\nR occurs {r} times\nU occurs {u} times\nE occurs {e} times"
          f"\nL occurs {l} times\nO occurs {o} times\nV occurs {v} times\nE occurs {e_in_love} times"
          f"\nLove score = {str(t + r + u + e)}{str(l + o + v + e)}")

calculate_love_score(first_name, second_name)


