
with open("./Input/Names/invited_names.txt") as invited_guests:
    name = invited_guests.readlines()
    # print(name)

with open("./Input/Letters/starting_letter.txt", mode = "r") as letter:
    guest_letter = letter.read()
    # print(guest_letter)

name_holder = "[name]"

for item in name:
    trimmed_item  = item.strip()
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        guest_letter = letter.read()

    if name_holder in guest_letter:
        # print(item)
        # print("yes")
        # print(guest_letter)
        replacement = guest_letter.replace(name_holder, trimmed_item )
        # print(replacement)

        with open(f"./Completed_list/BirthdayCeremonyParticipants/{trimmed_item}.txt", mode = "w") as participants_letter:
            participants_letter.write(replacement)
            # print(participants)
