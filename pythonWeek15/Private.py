class Student:
    # Constructor to initialize Student attributes
    def __init__(self, schoolName, departmentHead, studentName, studentID, studentAddress, credits, gpa):
        
        # Initialize instance variables with provided values
        self._schoolName = schoolName
        self._departmentHead = departmentHead
        self._studentName = studentName
        self._studentID = studentID
        self._studentAddress = studentAddress
        self._credits = credits
        self._gpa = gpa

    # Getter and setter for SchoolName attribute
    @property
    def SchoolName(self):
        print(f'"{self._schoolName}"was accessed')
        return self._schoolName

    @SchoolName.setter
    def SchoolName(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("School Name must be a string.")
        
        print(f'"{self._schoolName}"is now "{value}".')
        self._schoolName = value

    @SchoolName.deleter
    def SchoolName(self):
        print(f'"{self._schoolName}"was deleted')
        del self._schoolName


    # Getter and setter for DepartmentHead attribute
    @property
    def DepartmentHead(self):
        print(f'"{self._departmentHead}"was accessed')
        return self._departmentHead

    @DepartmentHead.setter
    def DepartmentHead(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Department Head must be a string.")

        print(f'"{self._departmentHead}"is now "{value}".')
        self._departmentHead = value

    @DepartmentHead.deleter
    def DepartmentHead(self):
        print(f'"{self._departmentHead}"was deleted')
        del self._departmentHead

    # Getter and setter for StudentName attribute
    @property
    def StudentName(self):
        print(f'"{self._studentName}"was accessed')
        return self._studentName

    @StudentName.setter
    def StudentName(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Student Name must be a string.")
        
        print(f'"{self._studentName}"is now "{value}".')
        self._studentName = value

    @StudentName.deleter
    def StudentName(self):
        print(f'"{self._studentName}"was deleted')
        del self._studentName


    # Getter and setter for StudentID attribute
    @property
    def StudentID(self):
        print(f'"{self._studentID}"was accessed')
        return self._studentID

    @StudentID.setter
    def StudentID(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Student ID must be a string.")
        
        print(f'"{self._studentID}"is now "{value}".')
        self._studentID = value

    @StudentID.deleter
    def StudentID(self):
        print(f'"{self._studentID}"was deleted')
        del self._studentID

    # Getter and setter for StudentAddress attribute
    @property
    def StudentAddress(self):
        print(f'"{self._studentAddress}"was accessed')
        return self._studentAddress

    @StudentAddress.setter
    def StudentAddress(self, value):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Student Address must be a string.")
        
        print(f'"{self._studentAddress}"is now "{value}".')
        self._studentAddress = value

    @StudentAddress.deleter
    def StudentAddress(self):
        print(f'"{self._studentAddress}"was deleted')
        del self._studentAddress

    # Getter and setter for Credits attribute
    @property
    def Credits(self):
        print(f'"{self._credits}"was accessed')
        return self._credits

    @Credits.setter
    def Credits(self, value):
        # Check if the value is a positive integer
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Credits must be a positive integer.")
        
        print(f'"{ self._credits}"is now "{value}".')
        self._credits = value
    
    @Credits.deleter
    def Credits(self):
        print(f'"{self._credits}"was deleted')
        del self._credits

    # Getter and setter for GPA attribute
    @property
    def GPA(self):
        print(f'"{self._gpa}"was accessed')
        return self._gpa

    @GPA.setter
    def GPA(self, value):
        # Check if the value is within the valid GPA range
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0.")
        
        print(f'"{self._gpa}"is now "{value}".')
        self._gpa = value
    
    @GPA.deleter
    def GPA(self):
        print(f'"{ self._gpa}"was deleted')
        del  self._gpa
        
# Sample data
student1 = Student("NTU", "Cai Chengxiu", "Lisa", "S001", "no.87,Tainan", 87, 3.7)
print(student1.GPA)

# Change schoolName test
student1.SchoolName = "TUT"
print(student1.SchoolName)
