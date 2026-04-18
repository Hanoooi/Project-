import numpy as np
import pandas as pd

data = {
    "Student_ID": range(101, 121),
    "Name": [
        "Ali", "Sara", "Ahmed", "Fatima", "Noor",
        "Omar", "Huda", "Yousef", "Aisha", "Khalid",
        "Maryam", "Salman", "Zainab", "Hassan", "Laila",
        "Bilal", "Amna", "Tariq", "Reem", "Imran"
    ],
    "Department": [
        "CS", "IT", "CS", "Math", "IT",
        "CS", "Math", "IT", "CS", "Math",
        "CS", "IT", "Math", "CS", "IT",
        "Math", "CS", "IT", "Math", "CS"
    ],
    "Maths": [78, 85, 90, 88, 76, 95, 67, 80, 89, 72,
              91, 84, 73, 86, 79, 66, 92, 81, 70, 88],
    "Python": [82, 78, 88, 90, 74, 96, 69, 85, 91, 70,
               94, 80, 75, 87, 83, 68, 95, 84, 72, 89],
    "Statistics": [75, 80, 85, 88, 70, 92, 65, 78, 90, 68,
                   89, 82, 71, 84, 77, 64, 91, 79, 69, 86],
    "Attendance": [85, 90, 95, 92, 70, 98, 65, 88, 96, 75,
                   93, 89, 73, 90, 85, 68, 97, 86, 74, 91]
}

df = pd.DataFrame(data)

maths = np.array(df["Maths"])
python_marks = np.array(df["Python"])
stats = np.array(df["Statistics"])

print("Maths highest mark:", maths.max())
print("Maths lowest mark:", maths.min())
print("Maths average:", maths.mean())
print("Maths median:", np.median(maths))
print("Maths standard deviation:", maths.std())

bonus_maths = maths + 5
students_above_80 = maths > 80

df["Total"] = df[["Maths", "Python", "Statistics"]].sum(axis=1)
df["Average"] = df["Total"] / 3

def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

print("\nTop 3 performing students:")
print(df.sort_values("Average", ascending=False).head(3)[["Name", "Average"]])

print("\nStudents with attendance below 75:")
print(df[df["Attendance"] < 75][["Name", "Attendance"]])

print("\nDepartment-wise average marks:")
print(df.groupby("Department")["Average"].mean())

print("\nStudents who scored more than 80 in Python:")
print(df[df["Python"] > 80][["Name", "Python"]])

print("\nGrade distribution:")
print(df["Grade"].value_counts())

df.to_csv("students.csv", index=False)

print("\nStudent data saved as students.csv")
