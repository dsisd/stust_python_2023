class Student:
    # Constructor to initialize Student attributes
    def __init__(self, schoolName, departmentHead, studentName, studentID, studentAddress, credits, gpa):
        # Initialize instance variables with provided values
        self.schoolName = schoolName
        self.departmentHead = departmentHead
        self.studentName = studentName
        self.studentID = studentID
        self.studentAddress = studentAddress
        self.credits = credits
        self.gpa = gpa

    # Getter and setter for SchoolName attribute
    @property
    def SchoolName(self):
        return self.schoolName

    @SchoolName.setter
    def SchoolName(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("School Name must be a string.")
        self.schoolName = value

    # Getter and setter for DepartmentHead attribute
    @property
    def DepartmentHead(self):
        return self.departmentHead

    @DepartmentHead.setter
    def DepartmentHead(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Department Head must be a string.")
        self.departmentHead = value

    # Getter and setter for StudentName attribute
    @property
    def StudentName(self):
        return self.studentName

    @StudentName.setter
    def StudentName(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Student Name must be a string.")
        self.studentName = value

    # Getter and setter for StudentID attribute
    @property
    def StudentID(self):
        return self.studentID

    @StudentID.setter
    def StudentID(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Student ID must be a string.")
        self.studentID = value

    # Getter and setter for StudentAddress attribute
    @property
    def StudentAddress(self):
        return self.studentAddress

    @StudentAddress.setter
    def StudentAddress(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Student Address must be a string.")
        self.studentAddress = value

    # Getter and setter for Credits attribute
    @property
    def Credits(self):
        return self.credits

    @Credits.setter
    def Credits(self, value):
        # Check if the value is a positive integer
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Credits must be a positive integer.")
        self.credits = value

    # Getter and setter for GPA attribute
    @property
    def GPA(self):
        return self.gpa

    @GPA.setter
    def GPA(self, value):
        # Check if the value is within the valid GPA range
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0.")
        self.gpa = value

# Sample data
student1 = Student("NTU", "Cai Chengxiu", "Lisa", "S001", "no.87,Tainan", 87, 3.7)
print(student1.GPA)

# Change schoolName test
student1.SchoolName = "TUT"
print(student1.SchoolName)
