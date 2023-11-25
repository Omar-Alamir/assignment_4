student_data = [
     {"ID": 1, "Name": "Alice", "Age": 20, "Major": "CS", "GPA": 3.7},
     {"ID": 2, "Name": "Bob", "Age": 21, "Major": "CCE", "GPA": 3.9}]


def main(): 

 user_input = int(input("Enter user ID"))
 student_by_ID(user_input)



def student_by_ID (x):
    print(student_data ["ID" : x, "Name"])




main()