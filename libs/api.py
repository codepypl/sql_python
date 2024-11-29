def list_students_with_courses(db):
    query = """
    select st.imie, st.nazwisko, k.nazwa_kursu from studenci as st
    left join student_kurs as sk on sk.student_id=st.student_id
    left join kursy k on sk.kurs_id = k.kurs_id
    """
    results = db.execute_query(query, db_name='uczelnia')
    return results

def list_courses_by_department(db, department_name):
    query = f"""
    select nazwa_kursu from kursy k
    right join wydzialy w on k.wydzial_id = w.wydzial_id
    where w.nazwa_wydzialu = '{department_name}';
    """
    results = db.execute_query(query, db_name='uczelnia')
    return results
def show_grades_for_student(db, student_id=None, student_name=None):
    query = f"""
    SELECT O.ocena, K.nazwa_kursu
    FROM oceny O
    JOIN kursy K ON O.kurs_id = K.kurs_id
    JOIN studenci S ON O.student_id = S.student_id
    WHERE S.nazwisko = '{student_name}' OR S.student_id = {student_id}
    """
    results = db.execute_query(query, db_name='uczelnia')
    return results


def update_student_age(db, student_id, new_age):
    db.update_record('studenci', f'wiek = {new_age}', f'student_id = {student_id}', db_name='uczelnia')

def update_lecturer_name(db, lecturer_id, new_name=None, new_surname=None):
    if new_name is not None:
        db.update_record('prowadzacy', f'imie = "{new_name}"', f'prowadzacy_id = {lecturer_id}', db_name='uczelnia')
    if new_surname is not None:
        db.update_record('prowadzacy', f'nazwisko = "{new_surname}"', f'prowadzacy_id = {lecturer_id}', db_name='uczelnia')

def delete_unused_course(db, course_id):
    query = f"SELECT COUNT(*) FROM student_kurs WHERE kurs_id = {course_id}"
    result = db.select_records(query, db_name='uczelnia')
    if result[0][0] == 0:
        db.delete_record('kursy', f'kurs_id = {course_id}', db_name='uczelnia')

def delete_student_with_grades(db, student_id):
    db.delete_record('oceny', f'student_id = {student_id}', db_name='uczelnia')
    db.delete_record('studenci', f'student_id = {student_id}', db_name='uczelnia')

def find_students_with_course_and_lecturer(db):
    query = """
    SELECT S.imie, S.nazwisko, K.nazwa_kursu, P.imie, P.nazwisko
    FROM studenci S
    JOIN student_kurs SK ON S.student_id = SK.student_id
    JOIN kursy K ON SK.kurs_id = K.kurs_id
    JOIN prowadzacy P ON K.prowadzacy_id = P.prowadzacy_id
    """
    results = db.execute_query(query, db_name='uczelnia')
    return results

def list_departments_with_course_count(db):
    query = """
    SELECT W.nazwa_wydzialu, COUNT(K.kurs_id)
    FROM wydzialy W
    LEFT JOIN kursy K ON W.wydzial_id = K.wydzial_id
    GROUP BY W.nazwa_wydzialu
    """
    results = db.execute_query(query, db_name='uczelnia')
    return results

def find_students_with_high_grades(db):
    query = """
    SELECT DISTINCT S.imie, S.nazwisko
    FROM studenci S
    JOIN oceny O ON S.student_id = O.student_id
    WHERE O.ocena > 4.0
    """
    results = db.execute_query(query, db_name='uczelnia')
    return results

def average_grade_for_courses(db):
    query = """
    SELECT K.nazwa_kursu, AVG(O.ocena)
    FROM kursy K
    JOIN oceny O ON K.kurs_id = O.kurs_id
    GROUP BY K.nazwa_kursu
    """
    results = db.execute_query(query, db_name='uczelnia')
    return results
