import json

def generate_report(json_file_path: str) -> dict:
    with open(json_file_path, "r", encoding="utf-8") as file:
        tasks = json.load(file)

    report = {}
    for task in tasks:
        if task.get("status") == "completed":
            assignee = task.get("assignee")
            report[assignee] = report.get(assignee, 0) + 1


    return report
if __name__ == "__main__":
    report = generate_report("tasks.json")
    print(report)