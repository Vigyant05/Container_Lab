import csv

def read_csv(filename):
    students=[]
    with open(filename,newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            students.append((row['Name'], int(row['Marks'])))
    return students

def draw_bar_chart(data):
    print("Student Marks Visualization")

    max_name_len=max(len(name) for name,_ in data)
    max_marks=max(marks for _,marks in data)

    for name,marks in data:
        bar='█' *(marks*50//max_marks)
        print(f"{name.ljust(max_name_len)} | {bar} {marks}")

if __name__=="__main__":
    students=read_csv("students.csv")
    draw_bar_chart(students)