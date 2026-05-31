students = {
    "Alice": {"math":90, "science":80},
    "Bob": {"math":70, "science":85},
    "Charlie": {"math":88, "science":92}
}
name = input("Enter student name: ")
scores = students[name].values()
print("Average:", sum(scores)/len(scores))
