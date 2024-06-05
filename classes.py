from data import Database


class Base:

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}' """
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {data} """
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Country:
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date

    @staticmethod
    def select(table="country"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="country"):
        query = f"""INSERT INTO {table}(name, date) VALUES ('{self.name}','{self.date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}' """
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = {data} """
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class City:
    def __init__(self, name: str, country_id: int, date: str):
        self.name = name
        self.country_id = country_id
        self.date = date

    @staticmethod
    def select(table="city"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="city"):
        query = f""" INSERT INTO {table}(name, country_id, date) VALUES ('{self.name}',{self.country_id},'{self.date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="city"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}' """
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="city"):
        query = f"""DELETE FROM {table} WHERE {column} = {data} """
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Address:
    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id

    @staticmethod
    def select(table="address"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="address"):
        query = f""" INSERT INTO {table}(name, city_id) VALUES ('{self.name}',{self.city_id})"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="address"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="address"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Users:
    def __init__(self, first_name, last_name, username, password, gmail, last_update, created_at):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gmail = gmail
        self.last_update = last_update
        self.created_at = created_at

    @staticmethod
    def select(table="users"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="users"):
        query = f""" INSERT INTO {table}(first_name, last_name, password, gmail ,last_update,created_at) VALUES 
        ('{self.first_name}', '{self.last_name}', '{self.password}', '{self.gmail}', '{self.last_update}', '{self.created_at}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="users"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="users"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Student(Users):
    def __init__(self, first_name, last_name, username, password, gmail, last_update, created_at, balance,
                 active_courses):
        super().__init__(first_name, last_name, username, password, gmail, last_update, created_at)
        self.balance = balance
        self.active_courses = active_courses

    @staticmethod
    def select(table="student"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="student"):
        query = f""" INSERT INTO {table}(first_name, last_name, username, password, gmail ,last_update,created_at,balance,active_courses) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.username}','{self.password}',
        '{self.gmail}', '{self.last_update}', '{self.created_at}', '{self.balance}', '{self.active_courses}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="student"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="student"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Mentor:
    def __init__(self, first_name, last_name, username, password, gmail, status, last_update):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gmail = gmail
        self.status = status
        self.last_update = last_update
        # self.adress_id = adress_id

    @staticmethod
    def select(table="mentor"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="mentor"):
        query = f""" INSERT INTO {table}(first_name, last_name, username, password, gmail, status, last_update)
         VALUES ('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}', '{self.gmail}', '{self.status}','{self.last_update}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="mentor"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="mentor"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Course:
    def __init__(self, title, description, reyting, price, price_status, language):
        self.title = title
        self.description = description
        self.reyting = reyting
        self.price = price
        self.price_status = price_status
        self.language = language

    @staticmethod
    def select(table="course"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="course"):
        query = f""" INSERT INTO {table}(title, description, reyting, price,price_status, language) VALUES ('{self.title}',
        '{self.description}',{self.reyting},{self.price},'{self.price_status}','{self.language}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="course"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="course"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class CourseMentor:
    def __init__(self, course_id, mentor_id, last_update):
        self.course_id = course_id
        self.mentor = mentor_id
        self.last_update = last_update

    @staticmethod
    def select(table="course_mentor"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="course_mentor"):
        query = f""" INSERT INTO {table}(course_id, mentor_id, last_update) VALUES
        ({self.course_id},{self.mentor},'{self.last_update}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="course_mentor"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="course_mentor"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class CourseComents:
    def __init__(self, student_id, course_id, text, create_time):
        self.student_id = student_id
        self.course_id = course_id
        self.text = text
        self.create_time = create_time

    @staticmethod
    def select(table="course_comments"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="course_comments"):
        query = f""" INSERT INTO {table}(student_id, course_id,text,create_time) VALUES
        {self.student_id},{self.course_id},'{self.text}','{self.create_time}'
        )"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="course_comments"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="course_comments"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Basket:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    @staticmethod
    def select(table="basket"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="basket"):
        query = f""" INSERT INTO {table}(student_id, course_id) VALUES 
        ({self.student_id},{self.course_id})"""

        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="basket"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="basket"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Speciality:
    def __init__(self, title, description, courses_caount, last_update, create_date):
        self.title = title
        self.description = description
        self.courses_caount = courses_caount
        self.last_update = last_update
        self.create_date = create_date

    @staticmethod
    def select(table="speciality"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="speciality"):
        query = f""" INSERT INTO {table}(title, description, courses_caount, last_update, create_date) VALUES 
        ('{self.title}', '{self.description}',{self.courses_caount},'{self.last_update}','{self.create_date}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="speciality"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="speciality"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class SpecialityCourse:
    def __init__(self, speciality_id, course_id, last_update):
        self.speciality_id = speciality_id
        self.course_id = course_id
        self.last_update = last_update

    @staticmethod
    def select(table="speciality_course"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="speciality_course"):
        query = f""" INSERT INTO {table}(speciality_id, course_id, last_update) VALUES
        ({self.speciality_id},{self.course_id},'{self.last_update}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="speciality_course"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="speciality_course"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class CourseStudent:
    def __init__(self, course_id, student_id, last_update):
        self.course_id = course_id
        self.student_id = student_id
        self.last_update = last_update

    @staticmethod
    def select(table="course_student"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="course_student"):
        query = f""" INSERT INTO {table} (course_id, student_id, last_update) VALUES
        ({self.course_id},{self.student_id},'{self.last_update}');"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="course_student"):
        query = f""" DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="course_student"):
        query = f""" DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Modul:
    def __init__(self, name, lesson_count, lesson_update, create_date, course_id):
        self.name = name
        self.lesson_count = lesson_count
        self.lesson_update = lesson_update
        self.create_date = create_date
        self.course_id = course_id

    @staticmethod
    def select(table="modul"):
        query = f""" SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="modul"):
        query = f""" INSERT INTO {table}(name,lesson_count, lesson_update, create_date, course_id) VALUES 
        ('{self.name}',{self.lesson_count},)
        """
        return Database.connect(query, "insert")


class Lesson(Base):
    def __init__(self, name, modul_id):
        self.name = name
        self.modul_id = modul_id

    def insert(self, table):
        query = f""" INSERT INTO {table},(name,modul_id) VALUES ('{self.name}',{self.modul_id})"""
        return Database.connect(query, "insert")


class LessonComents(Base):
    def __init__(self, student_id, lesson_id, text):
        self.student_id = student_id
        self.lesson_id = lesson_id
        self.text = text

    def insert(self, table):
        query = f""" INSERT INTO {table}(student_id,lesson_id,text) VALUES
        ({self.student_id},{self.lesson_id},'{self.text}')
        )"""
        return Database.connect(query, "insert")


class PaymentStatus(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f""" INSERT INTO {table} VALUES ('{self.name}')"""
        return Database.connect(query, "insert")
