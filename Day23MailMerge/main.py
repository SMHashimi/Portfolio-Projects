
with open("./Input/Names/invited_names.txt") as invited_guests:
    name = invited_guests.readlines()
    # print(name)

with open("./Input/Letters/starting_letter.txt", mode = "r") as letter:
    guest_letter = letter.read()
    # print(guest_letter)

name_holder = "[name]"

for item in name:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        guest_letter = letter.read()

    if name_holder in guest_letter:
        # print(item)
        # print("yes")
        # print(guest_letter)
        replacement = guest_letter.replace(name_holder, item )
        print(replacement)

        with open("../Day23MailMerge/BirthdayCeremonyParticipants/InvitationForToph.txt", mode = "w") as toph:
            for_toph = toph.write(replacement)
























#
#
# for item in name:
#     people_to_be_invited =  item

