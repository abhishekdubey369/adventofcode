def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
    
    rules_section, updates_section = content.split("\n\n")
    
    rules = []
    for line in rules_section.splitlines():
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    
    updates = []
    for line in updates_section.splitlines():
        updates.append(list(map(int, line.split(','))))
    
    return rules, updates

def is_valid_order(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in position and y in position:
            if position[x] > position[y]:
                return False
    return True

def find_middle_page(update):
    n = len(update)
    return update[(n - 1) // 2]

def main(file_path):
    rules, updates = parse_input(file_path)
    
    valid_updates = []
    for update in updates:
        if is_valid_order(update, rules):
            valid_updates.append(update)
    
    middle_sum = sum(find_middle_page(update) for update in valid_updates)
    return middle_sum

file_path = "input_day5.txt"
result = main(file_path)
print(result)
