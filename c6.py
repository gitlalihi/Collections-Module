#Python program that accepts the number of subjects, subject names and marks. Input the number of subjects and then the subject name and marks separated by a space on the next line. Print the subject name and marks in order of appearance.
from collections import namedtuple
def main():
    num_subjects = int(input("Enter the number of subjects: "))
    Subject = namedtuple('Subject', ['name', 'marks'])
    subjects = []
    for i in range(num_subjects):
        subject, mark = input(f"Enter subject {i + 1} (name and marks separated by space): ").split()
        subjects.append(Subject(name=subject, marks=float(mark)))  
    print("\nSubject-wise marks:")
    for subject in subjects:
        print(f"{subject.name}: {subject.marks}")

if __name__ == "__main__":
    main()
