from classes import *


def servise_country():
    services = input("""
    ------------------------------------------------
    👉 Counter Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Country.select("country"):
            print(i)
        return servise_country()
    elif services == '2':
        name = input("Name : ")
        create_date = input("Date : ")
        country = Country(name, create_date)
        print(country.insert("country"))
        return servise_country()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "countr_id":
            print(Country.delete(column, date, "country"))

        else:
            print(Country.delete_id(column, date, "country"))
        return servise_country()
    elif services == "4":
        country = input("New Country : ")
        id = int(input("Country id : "))
        query = f"""
            UPDATE country SET name = '{country}' WHERE country_id = {id}
                                        """
        print(Country.update(query))
        return servise_country()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_country()


def servise_city():
    services = input("""
    ------------------------------------------------
    👉 City Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in City.select("city"):
            print(i)
        return servise_city()
    elif services == '2':
        name = input("Name : ")
        cauntr_id = int(input("Cauntr Id : "))
        date = input("Date : ")
        country = City(name, cauntr_id, date)
        print(country.insert("city"))
        return servise_city()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "countr_id":
            print(City.delete(column, date, "city"))

        else:
            print(City.delete_id(column, date, "city"))
        return servise_city()
    elif services == "4":
        country = input("New city : ")
        id = int(input("Country id : "))
        query = f"""
            UPDATE city SET name = '{country}' WHERE country_id = {id}
                                        """
        print(City.update(query))
        return servise_city()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_city()


def servise_address():
    services = input("""
    ------------------------------------------------
    👉 Address Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Address.select("address"):
            print(i)
        return servise_address()
    elif services == '2':
        name = input("Name : ")
        cauntr_id = int(input("City Id : "))
        country = Address(name, cauntr_id)
        print(country.insert("address"))
        return servise_address()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "city_id":
            print(Address.delete(column, date, "address"))

        else:
            print(Address.delete_id(column, date, "address"))
        return servise_address()
    elif services == "4":
        country = input("New city : ")
        id = int(input("Country id : "))
        query = f"""
            UPDATE address SET name = '{country}' WHERE address_id = {id}
                                        """
        print(Address.update(query))
        return servise_address()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_address()


def servise_users():
    services = input("""
    ------------------------------------------------
    👉 Users Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Users.select("users"):
            print(i)
        return servise_users()
    elif services == '2':
        first_name = (input("First Name : "))
        last_name = (input("Last Name"))
        username = input("Username : ")
        password = input("Password : ")
        email = input("Email : ")
        last_update = input("Last ")
        create_date = input("Date ")
        country = Users(first_name, last_name, username, password, email, last_update, create_date)
        print(country.insert("users"))
        return servise_users()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "user_id":
            print(Users.delete(column, date, "users"))

        else:
            print(Users.delete_id(column, date, "users"))
        return servise_users()
    elif services == "4":
        country = input("New city : ")
        id = int(input("User id : "))
        query = f"""
            UPDATE users SET first_name = '{country}' WHERE user_id = {id}
                                        """
        print(Users.update(query))
        return servise_users()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_users()


def servise_student():
    services = input("""
    ------------------------------------------------
    👉 Student Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Student.select("student"):
            print(i)
        return servise_student()
    elif services == '2':
        first_name = (input("First Name : "))
        last_name = (input("Last Name"))
        username = input("Username : ")
        password = input("Password : ")
        email = input("Email : ")
        last_update = input("Last ")
        create_date = input("Date ")
        balance = input("Balance : ")
        active = input("Active Courses : ")
        country = Student(first_name, last_name, username, password, email, last_update, create_date, balance, active)
        print(country.insert("student"))
        return servise_student()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "student_id":
            print(Student.delete(column, date, "student"))

        else:
            print(Student.delete_id(column, date, "student"))
        return servise_student()
    elif services == "4":
        country = input("New First Name : ")
        id = int(input("Student ID : "))
        query = f"""
            UPDATE student SET first_name = '{country}' WHERE student_id = {id}
                                        """
        print(Student.update(query))
        return servise_student()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_student()


def servise_mentor():
    services = input("""
    ------------------------------------------------
    👉 Mentorr Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Mentor.select("mentor"):
            print(i)
        return servise_mentor()
    elif services == '2':
        first_name = (input("First Name : "))
        last_name = (input("Last Name"))
        username = input("Username : ")
        password = input("Password : ")
        email = input("Email : ")
        status = input("Status : ")
        last_update = input("Last ")
        country = Mentor(first_name, last_name, username, password, email, status, last_update)
        print(country.insert("mentor"))
        return servise_mentor()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "mentor_id":
            print(Mentor.delete(column, date, "mentor"))

        else:
            print(Mentor.delete_id(column, date, "mentor"))
        return servise_mentor()
    elif services == "4":
        country = input("New First Name : ")
        id = int(input("Mentor ID : "))
        query = f"""
            UPDATE mentor SET first_name = '{country}' WHERE mentor_id = {id}
                                        """
        print(Mentor.update(query))
        return servise_mentor()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_mentor()


def servise_course():
    services = input("""
    ------------------------------------------------
    👉 Course Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Country.select("course"):
            print(i)
        return servise_course()
    elif services == '2':
        title = (input("Title : "))
        description = (input("Description : "))
        reting = int(input("Reting : "))
        price = int(input("Price : "))
        price_status = (input("Price Status : "))
        language = input("Language : ")

        country = Course(title, description, reting, price, price_status, language)
        print(country.insert("course"))
        return servise_course()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "course_id":
            print(Course.delete(column, date, "course"))

        else:
            print(Mentor.delete_id(column, date, "course"))
        return servise_course()
    elif services == "4":
        country = input("New Title : ")
        id = int(input("Course ID : "))
        query = f"""
            UPDATE course SET title = '{country}' WHERE course_id = {id}
                                        """
        print(Course.update(query))
        return servise_course()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_course()


def servise_course_mentor():
    services = input("""
    ------------------------------------------------
    👉 Course Mentor Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in CourseMentor.select("course_mentor"):
            print(i)
        return servise_course_mentor()
    elif services == '2':
        course_id = int(input("Course ID : "))
        mentor = int(input("Mentor iD : "))
        last_update = input("Last update : ")

        country = CourseMentor(course_id, mentor, last_update)
        print(country.insert("course_mentor"))
        return servise_course_mentor()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "course_mentor_id":
            print(CourseMentor.delete(column, date, "course_mentor"))

        else:
            print(CourseMentor.delete_id(column, date, "course_mentor"))
        return servise_course_mentor()
    elif services == "4":
        country = input("New Title : ")
        id = int(input("Course ID : "))
        query = f"""
            UPDATE course_mentor SET title = '{country}' WHERE course_id = {id}
                                        """
        print(CourseMentor.update(query))
        return servise_course_mentor()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_course_mentor()


def servise_course_coments():
    services = input("""
    ------------------------------------------------
    👉 Course Mentor Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in CourseComents.select("course_comments"):
            print(i)
        return servise_course_coments()
    elif services == '2':
        course_id = int(input("Student ID : "))
        mentor = int(input("Cours iD : "))
        text = input("Enter text :")
        last_update = input("Create Time : ")
        country = CourseComents(course_id, mentor, text, last_update)
        print(country.insert("course_comments"))
        return servise_course_coments()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "course_coments_id":
            print(CourseComents.delete(column, date, "course_comments"))

        else:
            print(CourseComents.delete_id(column, date, "course_comments"))
        return servise_course_coments()
    elif services == "4":
        country = input("New Title : ")
        id = int(input("Course ID : "))
        query = f"""
            UPDATE course_coments SET student_id = '{country}' WHERE course_coments_id = {id}
                                        """
        print(CourseMentor.update(query))
        return servise_course_mentor()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_course_mentor()


def servise_basket():
    services = input("""
    ------------------------------------------------
    👉 Basket Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Basket.select("basket"):
            print(i)
        return servise_basket()
    elif services == '2':
        student = int(input("Student Id : "))
        course = int(input("Course Id : "))
        country = Basket(student, course)
        print(country.insert("basket"))
        return servise_basket()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "basket_id":
            print(Basket.delete(column, date, "basket"))

        else:
            print(Basket.delete_id(column, date, "basket"))
        return servise_basket()
    elif services == "4":
        country = input("New student Id : ")
        id = int(input("Basket ID : "))
        query = f"""
            UPDATE basket SET student_id = '{country}' WHERE basket_id = {id}
                                        """
        print(Basket.update(query))
        return servise_basket()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_basket()


def servise_speciality_course():
    services = input("""
    ------------------------------------------------
    👉 Speciality Course Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in SpecialityCourse.select("speciality_course"):
            print(i)
        return servise_speciality_course()
    elif services == '2':
        speciality_id = int(input("Speciality Id"))
        course_id = int(input("Course Id"))
        last_update = input("Last Update : ")
        country = SpecialityCourse(speciality_id, course_id, last_update)
        print(country.insert("speciality_course"))
        return servise_speciality_course()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "speciality_course_id":
            print(SpecialityCourse.delete(column, date, "speciality_course"))

        else:
            print(SpecialityCourse.delete_id(column, date, "speciality_course"))
        return servise_speciality_course()
    elif services == "4":
        country = input("New Speciality Course Id : ")
        id = int(input("Speciality Course ID : "))
        query = f"""
            UPDATE speciality_course SET speciality_id = '{country}' WHERE speciality_course_id = {id}
                                        """
        print(SpecialityCourse.update(query))
        return servise_speciality_course()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_speciality_course()


def servise_speciality():
    services = input("""
    ------------------------------------------------
    👉 Speciality Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Speciality.select("speciality"):
            print(i)
        return servise_speciality()
    elif services == '2':
        title = (input("Title : "))
        description = (input("Description : "))
        courses_caount = int(input("Course Count"))
        last_update = (input("Last Update : "))
        create_date = (input("Create Date : "))
        country = Speciality(title, description, courses_caount, last_update, create_date)
        print(country.insert("speciality"))
        return servise_speciality()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "speciality_id":
            print(Speciality.delete(column, date, "speciality"))

        else:
            print(Speciality.delete_id(column, date, "speciality"))
        return servise_speciality()
    elif services == "4":
        country = input("New title Id : ")
        id = int(input("Speciality ID : "))
        query = f"""
            UPDATE speciality SET title = '{country}' WHERE speciality_id = {id}
                                        """
        print(Speciality.update(query))
        return servise_speciality()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_speciality()


def servise_course_student():
    services = input("""
       ------------------------------------------------
       👉 Course Student Table 
           1. Select
           2. Insert
           3. Delete
           4. Update
           5. Back
       ------------------------------------------------
       Enter : """)
    if services == '1':
        for i in CourseStudent.select("course_student"):
            print(i)
        return servise_course_student()
    elif services == '2':
        course_id = int(input("Course Id "))
        stuent_id = int(input("Student Id "))
        last_update = input("Last Update : ")
        country = CourseStudent(course_id, stuent_id, last_update)
        print(country.insert("course_student"))
        return servise_course_student()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "course_student_id":
            print(CourseStudent.delete(column, date, "course_student"))

        else:
            print(CourseStudent.delete_id(column, date, "course_student"))
        return servise_course_student()
    elif services == "4":
        country = input("New Course Id : ")
        id = int(input("Course student ID : "))
        query = f"""
               UPDATE course_student SET course_id = '{country}' WHERE course_student_id = {id}
                                           """
        print(CourseStudent.update(query))
        return servise_course_student()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_course_student()


def servise_lesson():
    services = input("""
           ------------------------------------------------
           👉 Lesson Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------
           Enter : """)
    if services == '1':
        for i in Lesson.select("lesson"):
            print(i)
        return servise_lesson()
    elif services == '2':
        name = input("Name : ")
        modul_id = int(input("Modul Id "))
        country = Lesson(name, modul_id)
        print(country.insert("lesson"))
        return servise_lesson()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "lesson_id":
            print(Lesson.delete(column, date, "lesson"))

        else:
            print(Lesson.delete_id(column, date, "lesson"))
        return servise_lesson()
    elif services == "4":
        country = input("New Name : ")
        id = int(input("Lesson ID : "))
        query = f"""
                   UPDATE lesson SET name = '{country}' WHERE lesson_id = {id}
                                               """
        print(Lesson.update(query))
        return servise_lesson()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_lesson()


def servise_lesson_coments():
    services = input("""
               ------------------------------------------------
               👉 Lesson Coments Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------
               Enter : """)
    if services == '1':
        for i in LessonComents.select("lesson_coments"):
            print(i)
        return servise_lesson_coments()
    elif services == '2':
        student_id = int(input("Student ID : "))
        lesson_id = int(input("Lesson ID : "))
        text = input("Text : ")
        country = LessonComents(student_id, lesson_id, text)
        print(country.insert("lesson_coments"))
        return servise_lesson_coments()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "lesson_coments_id":
            print(LessonComents.delete(column, date, "lesson_coments"))

        else:
            print(LessonComents.delete_id(column, date, "lesson_coments"))
        return servise_lesson_coments()
    elif services == "4":
        country = input("Student Id : ")
        id = int(input("Lesson Coments ID : "))
        query = f"""
                       UPDATE lesson_coments SET student_id = '{country}' WHERE lesson_coments_id = {id}
                                                   """
        print(LessonComents.update(query))
        return servise_lesson_coments()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_lesson_coments()


def servise_payment_status():
    services = input("""
               ------------------------------------------------
               👉 Payment Status Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------
               Enter : """)
    if services == '1':
        for i in PaymentStatus.select("payment_status"):
            print(i)
        return servise_payment_status()
    elif services == '2':
        name = input("Name : ")
        country = PaymentStatus(name)
        print(country.insert("payment_status"))
        return servise_payment_status()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "payment_status_id":
            print(PaymentStatus.delete(column, date, "payment_status"))

        else:
            print(PaymentStatus.delete_id(column, date, "payment_status"))
        return servise_payment_status()
    elif services == "4":
        country = input("Name : ")
        id = int(input("Payment Status ID : "))
        query = f"""
                       UPDATE payment_status SET name = '{country}' WHERE payment_status = {id}
                                                   """
        print(PaymentStatus.update(query))
        return servise_payment_status()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_payment_status()


def main():
    tables = input("""
    __________________________________________________________________
         1. Country
         2. City
         3. Address
         4. User
         5. Student
         6. Mentor
         7. Course
         8. Course Mentor
         9. Course Comments
        10. Basket
        11. Speciality
        12. Speciality Course
        13. CourseStudent
        14. Modul
        15. Lesson
        16. LessonComments
        17. Payment Status
        18. Payment Type
        19. Payment
    _________________________________________________________
     👉👉👉  """)
    if tables == "1":
        return servise_country()
    elif tables == "2":
        return servise_city()
    elif tables == "3":
        return servise_address()
    elif tables == "4":
        return servise_users()
    elif tables == "5":
        return servise_student()
    elif tables == "6":
        return servise_mentor()
    elif tables == "7":
        return servise_course()
    elif tables == "8":
        return servise_course_mentor()
    elif tables == "9":
        return servise_course_coments()
    elif tables == "10":
        return servise_basket()
    elif tables == "11":
        return servise_speciality()
    elif tables == "12":
        return servise_speciality_course()
    elif tables == "13":
        return servise_course_student()
    elif tables == "14":
        return servise_lesson()
    elif tables == "15":
        return servise_lesson_coments()
    elif tables == "16":
        return servise_payment_status()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday Table mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return main()


if __name__ == "__main__":
    main()
