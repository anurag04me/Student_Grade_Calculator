import tkinter as tk

def calculate_grade():
    marks = [int(entry.get()) for entry in entries]
    total = sum(marks)
    avg = total / len(marks)

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "Fail"

    result_label.config(text=f"Total: {total}\nGrade: {grade}")

app = tk.Tk()
app.title("Student Grade Calculator")

entries = []
for i in range(5):
    tk.Label(app, text=f"Subject {i+1}:").grid(row=i, column=0)
    entry = tk.Entry(app)
    entry.grid(row=i, column=1)
    entries.append(entry)

tk.Button(app, text="Calculate", command=calculate_grade).grid(row=6, column=0, columnspan=2)
result_label = tk.Label(app, text="Total: \nGrade: ")
result_label.grid(row=7, column=0, columnspan=2)

app.mainloop()
