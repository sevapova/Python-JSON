
import json

with open("students.json", "r") as f:
    students = json.load(f)

students.sort(key=lambda s: int(s["score"]), reverse=True)

for i, student in enumerate(students, start=1):
    student["rank"] = i

with open("rating.json", "w") as f:
    json.dump(students, f,indent=4)

