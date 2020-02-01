from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

def main():
    alice = Student('Alice', 12345, 3.5)
    bob = Student('Bob', 98765, 2.75)

    print(alice)
    print(bob)

main()