menu_items = []
while 1:
    line = input()
    if line.lower() == "done":
        break
    else:
        parts = line.split(" #")
        menu_item = parts[0]
        if len(parts) == 2 and parts[1] == "N":
            menu_items.append(menu_item)
        else:
            menu_number = int(parts[1])
            if menu_number <= len(menu_items):
                menu_items.insert(menu_number - 1, menu_item)
            else:
                menu_items.append(menu_item)

print(f"Menu: {menu_items}")
