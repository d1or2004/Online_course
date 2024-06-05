from data import Database


def create_tables():
    country = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now(),
            date DATE);"""

    city = f"""
            CREATE TABLE city(
                city_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                country_id INT REFERENCES country(country_id),
                last_update TIMESTAMP DEFAULT now(),
                date DATE);"""

    address = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            city_id INT REFERENCES city(city_id));
    """
    users = f"""
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            password VARCHAR(20),
            gmail VARCHAR(20),
            last_update TIMESTAMP DEFAULT now(),
            created_at DATE);"""

    student = f"""
    CREATE TABLE student(
        student_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        username VARCHAR(20),
        password VARCHAR(20),
        gmail VARCHAR(20),
        last_update TIMESTAMP DEFAULT now(),
        created_at DATE,
        balance VARCHAR(30),
        active_courses VARCHAR(20));
    """

    mentor = f"""
        CREATE TABLE mentor(
        mentor_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        username VARCHAR(20),
        password VARCHAR(20),
        gmail VARCHAR(20),
        status VARCHAR(20),
        last_update TIMESTAMP DEFAULT now(),
        address_id INT REFERENCES address(address_id));"""

    course = f"""
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            title VARCHAR(20),
            description VARCHAR(20),
            reyting FLOAT,
            price SMALLINT,
            price_status VARCHAR(20),
            language VARCHAR(20));
    """
    course_mentor = f"""
    CREATE TABLE course_mentor(
        course_mentor_id SERIAL PRIMARY KEY,
        course_id INT REFERENCES course(course_id),
        mentor_id INT REFERENCES mentor(mentor_id),
        last_update TIMESTAMP DEFAULT now());
    """

    course_coments = f"""
        CREATE TABLE course_comments(
        course_comments_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES student(student_id),
        course_id INT REFERENCES course(course_id),
        text VARCHAR(200),
        create_time TIMESTAMP DEFAULT now()
        );
    """
    basket = f"""
    CREATE TABLE basket(
        basket_id  SERIAL PRIMARY KEY,
        student_id INT REFERENCES student(student_id),
        course_id INT REFERENCES course(course_id));
    """

    speciality = f"""
    CREATE TABLE speciality(
        speciality_id SERIAL PRIMARY KEY,
        title VARCHAR(200),
        description VARCHAR(100),
        courses_caount SMALLINT,
        last_update TIMESTAMP DEFAULT now(),
        create_date DATE);
        
    """

    speciality_course = f"""
    CREATE TABLE speciality_course(
        speciality_course_id SERIAL PRIMARY KEY,
        speciality_id INT REFERENCES speciality(speciality_id),
        course_id INT REFERENCES course(course_id),
        last_update TIMESTAMP DEFAULT now());
    """

    course_student = f"""
    CREATE TABLE course_student(
        course_student_id SERIAL PRIMARY KEY,
        course_id INT REFERENCES course(course_id),
        student_id INT REFERENCES student(student_id),
        last_update TIMESTAMP DEFAULT now());
    """

    modul = f"""
    CREATE TABLE modul(
        modul_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        lesson_count SMALLINT,
        last_update TIMESTAMP DEFAULT now(),
        create_date DATE,
        course_id INT REFERENCES course(course_id));
    """

    lesson = f"""
    CREATE TABLE lesson(
        lesson_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        modul_id INT REFERENCES modul(modul_id),
        last_update TIMESTAMP DEFAULT now());
    """

    lesson_coments = f"""
    CREATE TABLE lesson_coments(
        lesson_coments_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES student(student_id),
        lesson_id INT REFERENCES lesson(lesson_id),
        text VARCHAR(200),
        create_time TIMESTAMP DEFAULT now());
    """

    payment_status = f"""
        CREATE TABLE payment_status(
            payment_status_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now());
    """

    payment_type = f"""
        CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now());
    """
    payment = f"""
    CREATE TABLE payment(
    payment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(student_id),
    course_id INT REFERENCES course(course_id),
    amount SMALLINT,
    payment_status_id INT REFERENCES payment_status(payment_status_id),
    payment_type_id INT REFERENCES payment_type(payment_type_id),
    last_update TIMESTAMP DEFAULT now(),
    create_date DATE);
    """






    data_table = {
        "country": country,
        "city": city,
        "address": address,
        "users": users,
        "student": student,
        "mentor": mentor,
        "course": course,
        "course_mentor": course_mentor,
        "course_coments": course_coments,
        "basket": basket,
        "speciality": speciality,
        "speciality_course": speciality_course,
        "course_student": course_student,
        "modul": modul,
        "lesson": lesson,
        "lesson_coments": lesson_coments,
        "payment_status": payment_status,
        "payment_type": payment_type,
        "payment": payment
    }

    for i in data_table:
        print(f"{i} {Database.connect(data_table[i], "create")}")


