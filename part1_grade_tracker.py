
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
   
    name = student["name"].strip().title()

    
    roll = int(student["roll"])

    
    marks = list(map(int, student["marks_str"].split(", ")))

   
    is_valid = all(word.isalpha() for word in name.split())

    if is_valid:
        print(f"{name} → ✓ Valid name")
    else:
        print(f"{name} → ✗ Invalid name")

    
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================\n")


for student in cleaned_students:
    if student["roll"] == 103:
        name = student["name"]
        print("Special Output for Roll 103:")
        print(name.upper())
        print(name.lower())


# Task 2: Marks Analysis
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

def get_grade(m):
    if 90 <= m <= 100:
        return "A+"
    elif 80 <= m <= 89:
        return "A"
    elif 70 <= m <= 79:
        return "B"
    elif 60 <= m <= 69:
        return "C"
    else:
        return "F"

print(f"\nMarks Report for {student_name}")
for sub, m in zip(subjects, marks):
    print(f"{sub} : {m} ({get_grade(m)})")

total = sum(marks)
average = round(total / len(marks), 2)

max_marks = max(marks)
min_marks = min(marks)

highest_subject = subjects[marks.index(max_marks)]
lowest_subject = subjects[marks.index(min_marks)]

print("\nTotal Marks:", total)
print("Average:", average)
print(f"Highest: {highest_subject} ({max_marks})")
print(f"Lowest : {lowest_subject} ({min_marks})")

new_count = 0

run_input = input("\nDo you want to enter new subjects? (yes/no): ")

if run_input.lower() == "yes":
    while True:
        sub = input("\nEnter subject name (or 'done' to stop): ")

        if sub.lower() == "done":
            break

        mark_input = input("Enter marks (0-100): ")

        if not mark_input.isdigit():
            print("⚠ Invalid input! Enter numeric value.")
            continue

        mark = int(mark_input)

        if mark < 0 or mark > 100:
            print("⚠ Marks must be between 0 and 100.")
            continue

        subjects.append(sub)
        marks.append(mark)
        new_count += 1

updated_avg = round(sum(marks) / len(marks), 2)

print("\nNew subjects added:", new_count)
print("Updated Average:", updated_avg)


# Task 3: Class Performance
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nName              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
averages = []

topper = ""
top_avg = 0

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    averages.append(avg)

    status = "Pass" if avg >= 60 else "Fail"

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    if avg > top_avg:
        top_avg = avg
        topper = name

    print(f"{name:<18} | {avg:^7} | {status}")


class_avg = round(sum(averages) / len(averages), 2)

print("\nPassed:", pass_count)
print("Failed:", fail_count)
print(f"Topper: {topper} ({top_avg})")
print("Class Average:", class_avg)


# Task 4: String Manipulation
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print("1. Clean Essay:\n", clean_essay)

print("\n2. Title Case:\n", clean_essay.title())

count = clean_essay.count("python")
print("\n3. 'python' count:", count)

replaced = clean_essay.replace("python", "Python ")
print("\n4. Replaced:\n", replaced)

sentences = clean_essay.split(". ")
print("\n5. Sentences List:\n", sentences)

print("\n6. Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")

