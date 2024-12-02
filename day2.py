def left_right():
    with open('input_day2.txt', 'r') as f:
        lines = f.readlines()

    def is_safe(report):
        differences = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
        
        
        if not all(1 <= diff <= 3 for diff in differences):
            return False
        
        is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
        is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
        
        return is_increasing or is_decreasing

    def can_be_safe_with_one_removal(report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                return True
        return False

    safe_reports = 0
    for line in lines:
        report = list(map(int, line.split()))
        if is_safe(report) or can_be_safe_with_one_removal(report):
            safe_reports += 1

    print("Number of safe reports:", safe_reports)

left_right()
