# Class SN: B30

students = []

# ── TASK 1: COLLECT STUDENT DATA ──────────────────────────
while True:
    name = input("Enter student name (or 'done'): ").strip()
    if name.lower() == "done": break          # stop collecting
    if name == "":
        print("Name cannot be empty."); continue

    scores = []
    for i in range(1, 4):                     # collect 3 scores
        while True:
            try:
                score = int(input(f"Enter score {i}: "))
                if 0 <= score <= 100:
                    scores.append(score); break
                else: print("Enter a score between 0 and 100.")
            except ValueError: print("Numbers only please.")

    students.append({"name": name, "scores": scores, "average": 0, "grade": "", "status": ""})
    print("Student added.\n")


# ── TASK 2: CALCULATE AVERAGE, GRADE & STATUS ─────────────
for s in students:
    s["average"] = round(sum(s["scores"]) / 3, 1)

    # Assign grade based on average
    s["grade"] = "A" if s["average"] >= 80 else \
                 "B" if s["average"] >= 65 else \
                 "C" if s["average"] >= 50 else \
                 "D" if s["average"] >= 40 else "F"

    s["status"] = "PASS" if s["average"] >= 50 else "FAIL"


# ── TASK 3: FIND TOP PERFORMER (no max()) ─────────────────
top = None
for s in students:                            # manually check each student
    if top is None or s["average"] > top["average"]:
        top = s                               # update if higher average found


# ── TASK 4: FAILING & PERFECT SCORE LISTS ─────────────────
failing = [s["name"] for s in students if any(sc < 40  for sc in s["scores"])]
perfect = [s["name"] for s in students if any(sc == 100 for sc in s["scores"])]


# ── TASK 5: CLASS AVERAGE ──────────────────────────────────
class_avg = round(sum(s["average"] for s in students) / len(students), 1) if students else 0


# ── TASK 6: PRINT REPORT ──────────────────────────────────
print("\n========================================")
print("     STUDENT PERFORMANCE REPORT")
print("========================================\n")

for i, s in enumerate(students, 1):
    print(f"{i}. {s['name']}")
    print(f"   Scores: {s['scores']}  |  Average: {s['average']}  |  Grade: {s['grade']}  |  Status: {s['status']}\n")

print("========================================")
print(f"Class Average:                {class_avg}")
print(f"Top Performer:                {top['name']} ({top['average']})" if top else "Top Performer: None")
print(f"Students with failing scores: {', '.join(failing) if failing else 'None'}")
print(f"Students with perfect scores: {', '.join(perfect) if perfect else 'None'}")
print("========================================")


# ── TASK 7: SEARCH FOR A STUDENT ──────────────────────────
while True:
    search = input("\nSearch student (or 'exit'): ").strip()
    if search.lower() == "exit": print("Goodbye!"); break

    # Look for a name match (case-insensitive)
    match = next((s for s in students if s["name"].lower() == search.lower()), None)

    if match:
        print(f"\nName: {match['name']} | Scores: {match['scores']} | "
              f"Average: {match['average']} | Grade: {match['grade']} | Status: {match['status']}\n")
    else:
        print("Student not found.")