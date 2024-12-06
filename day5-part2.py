from collections import defaultdict, deque

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

def topological_sort(pages, rules):
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    
    pages_set = set(pages)
    for x, y in rules:
        if x in pages_set and y in pages_set:
            adj_list[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

def find_middle_page(update):
    n = len(update)
    return update[(n - 1) // 2]

def main(file_path):
    rules, updates = parse_input(file_path)
    
    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        if is_valid_order(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    
    corrected_updates = [topological_sort(update, rules) for update in invalid_updates]
    
    middle_sum_corrected = sum(find_middle_page(update) for update in corrected_updates)
    return middle_sum_corrected

file_path = "input_day5.txt"
result = main(file_path)
print(result)
