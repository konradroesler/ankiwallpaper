from main import fname_for_latex, get_cards, get_svg_file_names

file_names = get_svg_file_names()
cards = get_cards()

yes = 0
no = 0
both_found = 0
none_found = 0
for card in cards:
    front_found = False
    back_found = False
    if fname_for_latex(card[0]) in file_names:
        yes += 1
        front_found = True
    else:
        #  print(f'FRONT::({card[0]})')
        no += 1
    if fname_for_latex(card[1]) in file_names:
        yes += 1
        back_found = True
    else:
        # print(f'BACK::({card[1]})')
        no += 1
    if (front_found and not back_found) or (not front_found and back_found):
        print(f"JUST ONE FOUND ERROR::({card})")
    if front_found and back_found:
        both_found += 1
    if not front_found and not back_found:
        print(f"NONE FOUND ERROR::({card})")
        none_found += 1

print(both_found, none_found)