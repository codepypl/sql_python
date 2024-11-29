from libs.mysql_connector import Db
from data import structure as struct
from data import  dumy_data as data
from libs.api import *

db = Db(host='localhost', user='root', password='Das5ahec')
db.drop_database('uczelnia')
print(f'------rozpoczecie dzialania programu----')
# Utworzenie bazy danych - zad1
print(f'----- stworzenie bazy danych----')
db.create_database('uczelnia')

# Utworzenie tabel - zad2
print(f'------stworzenie tabeli studenci----')
db.create_table('studenci', struct.students_table, db_name='uczelnia')
print(f'------stworzenie tabeli wydzialy----')
db.create_table('wydzialy', struct.departments_table, db_name='uczelnia')
print(f'------stworzenie tabeli prowadzacy----')
db.create_table('prowadzacy', struct.lecturers_table, db_name='uczelnia')
print(f'------stworzenie tabeli kursy----')
db.create_table('kursy', struct.courses_table, db_name='uczelnia')
print(f'------stworzenie tabeli oceny----')
db.create_table('oceny', struct.grades_table, db_name='uczelnia')
print(f'------stworzenie tabeli przedmioty----')
db.create_table('przedmioty', struct.subjects_table, db_name='uczelnia')
print(f'------stworzenie tabeli student_kurs----')
db.create_table('student_kurs', struct.student_to_course, db_name='uczelnia')

# Wstawienie danych testowych - zad3
print(f'------wstawianie danych testowych do tabeli wydzialy----')
for values in data.department_values:
    db.insert_record('wydzialy', data.department_columns,
                     f"'{values[0]}', '{values[1]}', '{values[2]}'", db_name='uczelnia')

print(f'------wstawianie danych testowych do tabeli prowadzacy----')
for values in data.lecturer_values:
    db.insert_record('prowadzacy', data.lecturer_columns, f"'{values[0]}', '{values[1]}', '{values[2]}', {values[3]}", db_name='uczelnia')

print(f'------wstawianie danych testowych do tabeli kursy----')
for values in data.course_values:
    db.insert_record('kursy', data.course_columns, f"'{values[0]}', {values[1]}, {values[2]}", db_name='uczelnia')

print(f'------wstawianie danych testowych do tabeli studenci----')
for values in data.student_values:
    db.insert_record('studenci', data.student_columns, f"'{values[0]}', '{values[1]}', {values[2]}, '{values[3]}'", db_name='uczelnia')

print(f'------wstawianie danych testowych do tabeli oceny----')
for values in data.grade_values:
    db.insert_record('oceny', data.grade_columns, f"{values[0]}, {values[1]}, {values[2]}, '{values[3]}'", db_name='uczelnia')

print(f'------wstawianie danych testowych do tabeli przedmioty----')
for values in data.subject_values:
    db.insert_record('przedmioty', data.subject_columns, f"'{values[0]}', {values[1]}", db_name='uczelnia')

print(f'------wstawianie danych testowych do tabeli student_kurs----')
for values in data.student_course_values:
    db.insert_record('student_kurs', data.student_course_columns, f"{values[0]}, {values[1]}", db_name='uczelnia')

# operacje crud - zad4
# create
db.insert_record('studenci', data.student_columns, "'Łukasz', 'Nowak', 28, 'Gryfów-Śląski'", db_name='uczelnia')
db.insert_record('student_kurs', data.student_course_columns, "6, 2", db_name='uczelnia')
# read

# Lista wszystkich studentów wraz z nazwą kursu, w którym uczestniczą
print(list_students_with_courses(db))
#
# Lista wszystkich kursów dostępnych na danym wydziale
print(list_courses_by_department(db, 'Wydział informatyki'))
#
# Oceny danego studenta wraz z nazwą kursu
print(show_grades_for_student(db, 1))
#
# Aktualizacja wieku wybranego studenta oraz zmiana nazwy prowadzącego kursu
update_student_age(db, 1, 29)
update_lecturer_name(db, 1, new_name='Przemek', new_surname='Tomaszewski')
#
# delete
# # Usunięcie kursu, który nie jest przypisany do żadnego studenta ani przedmiotu
# delete_unused_course(db, 5)
#
# # Usunięcie studenta wraz ze wszystkimi jego ocenami z kursów
# delete_student_with_grades(db, 1)
#
# # Zadania analityczne - zad 5
# Znajdź i wyświetl imiona i nazwiska wszystkich studentów oraz nazwę kursu,
# na który są zapisani, wraz z nazwą prowadzącego.
print(find_students_with_course_and_lecturer(db))
# Wyświetl wydziały oraz liczbę kursów przypisanych do każdego z nich.
print(list_departments_with_course_count(db))
# Znajdź studentów, którzy otrzymali ocenę powyżej 4.0 z co najmniej jednego kursu.
print(find_students_with_high_grades(db))
#Wyświetlśredniąocenędlakażdegokursu.
print(average_grade_for_courses(db))

# zadanie 6 to plik api.py w katalogu libs