# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
# Isse,5/27/2025,Created Script
# Isse Odawa,5/28/2025 Updated Script
# ------------------------------------------------------------------------------------------ #
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollment.json"

# Define the Data Variables and constants
menu_choice: str = ''  # Hold the choice made by the user.
students: list = []  # a table of student data



#     """  This callas process read and write, and
#         also checks for error for file opening related  during read and write """
class FileProcessor:

    """  This callas process read and write, and
        also checks for error for file opening related  during read and write """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ this function reads from the JSON file into list of dictionary in to student_data """
        try:
            with open(file_name, "r") as file:
                student_data.clear()
                student_data.extend(json.load(file))
        except Exception as e:
            IO.output_error_messages("Error reading from file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):

        """ this function writes data into JSON file from list of dictionary in the student_data """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print("The following data was saved to file!")
            IO.output_students_courses(student_data)
        except Exception as e:
            IO.output_error_messages("Error writing to file.", e)

# This class IO provides functions that outputs related error, menu, data and inputs from user for data collection
class IO:
    """
    This class IO provides functions that outputs related error,
    menu, data and inputs from user for data collection
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        this function return messages either errors two of them if necessary
        :param message:
        :param error:
        :return:
        """
        print(message)
        if error:
            print("-- Technical Error Message --")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        """
        This function provided menu option to user
        :param menu:
        :return:
        """
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """

        :return:
        """
        return input("What would you like to do: ")

    @staticmethod
    def output_students_courses(student_data: list):

        print("-" * 50)
        for student in student_data:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function takes inputs from user, a
        nd also checks for proper name inputs, missing inputs
        :param student_data:
        :return:
        """
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": first_name, "LastName": last_name, "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {first_name} {last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Invalid name entry.", e)
        except Exception as e:
            IO.output_error_messages("There was a problem with your entered data.", e)


# Main Body of Script
# Class processor is initiating read_data_from function
# with two arguments of FILE_Name and student data.
# this class is being initiated here because
# data for file and students are performed above class and functions
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    """
    IO class is performed with the 
    use output function to present menu to user
    """
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)
        """
           IO class use input_student_data function to
           accept student inputs
           """
    elif menu_choice == "2":
        IO.output_students_courses(students)
        """  IO class performs output function
         to presents student names and course name
                 """
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        """
        Class FileProcessor initiates write data function 
        to store students data in the the file
        """
    elif menu_choice == "4":
        break
    else:
        IO.output_error_messages("Please only choose option 1, 2, 3, or 4.")
        """
        class IO is initiate if there is error in user inputs  
        """

print("Program Ended")

