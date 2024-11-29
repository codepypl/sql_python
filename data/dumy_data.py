student_columns = "imie, nazwisko, wiek, miasto"
student_values = [
    ("Adam", "Kowalski", 21, "Warszawa"),
    ("Magda", "Nowak", 22, "Kraków"),
    ("Jan", "Wiśniewski", 23, "Gdańsk"),
    ("Anna", "Wójcik", 20, "Poznań"),
    ("Piotr", "Kowalczyk", 24, "Wrocław")
]
department_columns = "nazwa_wydzialu, dziekan, lokalizacja"
department_values = [
    ("Wydział Informatyki", "Dr. Jan Kowalski", "Warszawa"),
    ("Wydział Matematyki", "Dr. Anna Nowak", "Kraków"),
    ("Wydział Fizyki", "Dr. Piotr Wiśniewski", "Gdańsk")
]
lecturer_columns = "imie, nazwisko, tytul, wydzial_id"
lecturer_values = [
    ("Marek", "Zieliński", "Profesor", 1),
    ("Elżbieta", "Wiśniewska", "Doktor", 2),
    ("Paweł", "Kamiński", "Doktor", 3)
]
course_columns = "nazwa_kursu, wydzial_id, prowadzacy_id"
course_values = [
    ("Podstawy Informatyki", 1, 1),
    ("Analiza Matematyczna", 2, 2),
    ("Fizyka Kwantowa", 3, 3)
]
grade_columns = "student_id, kurs_id, ocena, data_oceny"
grade_values = [
    (1, 1, 5.0, '2024-01-01'),
    (2, 2, 4.5, '2024-01-01'),
    (3, 3, 4.0, '2024-01-01'),
    (4, 1, 3.5, '2024-01-01'),
    (5, 2, 4.0, '2024-01-01')
]
subject_columns = "nazwa_przedmiotu, kurs_id"
subject_values = [
    ("Wprowadzenie do programowania", 1),
    ("Równania różniczkowe", 2),
    ("Mechanika kwantowa", 3)
]
student_course_columns = "student_id, kurs_id"
student_course_values = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 1),
    (5, 2)
]
