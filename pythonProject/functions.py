# Team Members:-  Alpesh

list_of_courses = ["Data Science and Machine Learning",
                   "Python Programming",
                   "Careers In Artificial Intelligence and Machine",
                   "Introduction to Artificial Intelligence",
                   "Big Data Fundamentals - Data Storage Networking",
                   "Professional Communication"]
dict_of_courses = {
                   "Data Science and Machine Learning": 10,
                   "Python Programming": 20,
                   "Careers In Artificial Intelligence and Machine": 30,
                   "Introduction to Artificial Intelligence": 30,
                   "Big Data Fundamentals - Data Storage Networking": 20,
                   "Professional Communication": 10
}

############################################################################################

def courses(course_list):
    sum = 0
    for course in course_list:
        print(f'Enter marks for the course: {course}')
        sum = sum + int(input())
    return sum/len(course_list)

#############################################################################################

def courses_1(course_list):
    sum = 0
    for course in course_list:
        print(f'Enter marks for the course: {course}')
        sum = sum + int(input())
    print(sum/len(course_list))

############################################################################################

def arbitrary_func(*course_marks):
    sum = 0
    for marks in course_marks:
        sum = sum + marks
    print("Avg of all courses = ",sum/len(course_marks))

############################################################################################

def print_dict(courses_dict):
    sum = 0
    for course, marks in courses_dict.items():
        print(f"Marks obtained in {course} is {marks}")
        sum = sum + marks
    print(sum / len(courses_dict))

############################################################################################

def keyword_arg(**kwargs):
    sum = 0
    for marks in kwargs.values():
        sum = sum + int(marks)
    print(sum / len(kwargs))

############################################################################################

#function Call 1
print("Avg of all courses = ",courses(list_of_courses))

#function Call 2
courses_1

#function Call 3
arbitrary_func(10,20,30,20,10,40)

#function Call 4
print_dict(dict_of_courses)

#function Call 5
keyword_arg(Data_Science_and_Machine_Learning = "10",
                   Python_programming = "20",
                   Careers_In_Artificial_Intelligence_and_Machine = "30",
                   Introduction_to_Artificial_Intelligence = "30",
                   Big_Data_Fundamentals_Data_Storage_Networking =  "20",
                   Professional_Communication = "10")
