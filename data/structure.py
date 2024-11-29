students_table = """
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    wiek INT,
    miasto VARCHAR(50)
"""
departments_table = """
    wydzial_id INT AUTO_INCREMENT PRIMARY KEY,
    nazwa_wydzialu VARCHAR(100),
    dziekan VARCHAR(50),
    lokalizacja VARCHAR(100)
"""
lecturers_table ="""
    prowadzacy_id INT AUTO_INCREMENT PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    tytul VARCHAR(50),
    wydzial_id INT,
    FOREIGN KEY (wydzial_id) REFERENCES Wydzialy(wydzial_id)
"""
courses_table = """
    kurs_id INT AUTO_INCREMENT PRIMARY KEY,
    nazwa_kursu VARCHAR(100),
    wydzial_id INT,
    prowadzacy_id INT,
    FOREIGN KEY (wydzial_id) REFERENCES Wydzialy(wydzial_id),
    FOREIGN KEY (prowadzacy_id) REFERENCES Prowadzacy(prowadzacy_id)
"""

grades_table = """
    ocena_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    kurs_id INT,
    ocena DECIMAL(3, 2),
    data_oceny DATE,
    FOREIGN KEY (student_id) REFERENCES Studenci(student_id),
    FOREIGN KEY (kurs_id) REFERENCES Kursy(kurs_id)
"""
subjects_table= """
    przedmiot_id INT AUTO_INCREMENT PRIMARY KEY,
    nazwa_przedmiotu VARCHAR(100),
    kurs_id INT,
    FOREIGN KEY (kurs_id) REFERENCES Kursy(kurs_id)
"""
student_to_course = """
    student_id INT,
    kurs_id INT,
    PRIMARY KEY (student_id, kurs_id),
    FOREIGN KEY (student_id) REFERENCES Studenci(student_id),
    FOREIGN KEY (kurs_id) REFERENCES Kursy(kurs_id)
"""