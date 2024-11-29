def list_students_with_courses(db):
    res = db.select_records(
        table_name='studenci as st',
        columns='st.imie, st.nazwisko,k.nazwa_kursu',
        joins = [
                "LEFT JOIN student_kurs as sk ON sk.student_id = st.student_id",
                "LEFT JOIN kursy as k ON sk.kurs_id = k.kurs_id"]
        ,db_name='uczelnia')
    return res



def list_courses_by_department(db, department_name):
    res = db.select_records(
        table_name='kursy as k',
        columns='k.nazwa_kursu',
        joins = [
                "LEFT JOIN wydzialy as w ON w.wydzial_id = k.wydzial_id"
            ],
        condition=f"w.nazwa_wydzialu = '{department_name}'",
        db_name='uczelnia')
    return res

def show_grades_for_student(db, student_id=None, student_name=None):
    res = db.select_records(
        table_name='oceny as O',
        columns='O.ocena, K.nazwa_kursu',
        joins = [
                "LEFT JOIN kursy as K ON K.kurs_id = O.kurs_id",
                "LEFT JOIN studenci as S ON S.student_id = O.student_id"
            ],
        condition=f"S.student_id = {student_id} OR S.nazwisko = '{student_name}'",
        db_name='uczelnia')
    return res


def update_student_age(db, student_id, new_age):
    db.update_record('studenci', f'wiek = {new_age}', f'student_id = {student_id}', db_name='uczelnia')

def update_lecturer_name(db, lecturer_id, new_name=None, new_surname=None):
    if new_name is not None:
        db.update_record('prowadzacy', f'imie = "{new_name}"', f'prowadzacy_id = {lecturer_id}', db_name='uczelnia')
    if new_surname is not None:
        db.update_record('prowadzacy', f'nazwisko = "{new_surname}"', f'prowadzacy_id = {lecturer_id}', db_name='uczelnia')

def delete_unused_course(db):
    res = db.select_records(
        table_name='kursy as k',
        columns='k.kurs_id',
        joins = [
                "LEFT JOIN student_kurs as sk ON sk.kurs_id = k.kurs_id",
        ],
        condition=f"sk.kurs_id IS NULL",
        db_name='uczelnia')

    delete_course = db.delete_record(
        table_name='kursy',
        condition=f"kurs_id = {res[0][0]}",
        db_name='uczelnia'
    )
    return delete_course




def delete_student_with_grades(db, student_id):
    db.delete_record('oceny', f'student_id = {student_id}', db_name='uczelnia')
    db.delete_record('student_kurs', f'student_id = {student_id}', db_name='uczelnia')
    db.delete_record('studenci', f'student_id = {student_id}', db_name='uczelnia')

def find_students_with_course_and_lecturer(db):
    res = db.select_records(
        table_name='studenci as s',
        columns='s.imie, s.nazwisko, k.nazwa_kursu, p.imie, p.nazwisko',
        joins = [
                    "LEFT JOIN student_kurs SK ON S.student_id = SK.student_id",
                    "JOIN kursy K ON SK.kurs_id = K.kurs_id",
                    "JOIN prowadzacy P ON K.prowadzacy_id = P.prowadzacy_id"
        ],
        db_name='uczelnia'
    )
    return res

def list_departments_with_course_count(db):
    res = db.select_records(
        table_name='wydzialy as w',
        columns='w.nazwa_wydzialu, COUNT(k.kurs_id)',
        joins = [
                "LEFT JOIN kursy as k ON k.wydzial_id = w.wydzial_id"
            ],
        group_by='w.nazwa_wydzialu',
        db_name='uczelnia'
    )
    return res


def find_students_with_high_grades(db):
    res = db.select_records(
        table_name='studenci as s',
        columns='s.imie, s.nazwisko',
        joins = [
                "LEFT JOIN oceny as o ON o.student_id = s.student_id"
            ],
        condition= f"o.ocena > 4.0",
        group_by='s.student_id',
        db_name='uczelnia'
    )
    return res


def average_grade_for_courses(db):
    res = db.select_records(
        table_name='kursy as k',
        columns='k.nazwa_kursu, AVG(o.ocena)',
        joins = [
                "LEFT JOIN oceny as o ON o.kurs_id = k.kurs_id"
            ],
        group_by='k.nazwa_kursu',
        db_name='uczelnia'
    )
    return res

