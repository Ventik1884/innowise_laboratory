sql
-- 1. Создание таблицы students
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

-- 2. Создание таблицы grades
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 3. Вставка данных в students
INSERT INTO students (full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- 4. Вставка данных в grades
INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
    (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
    (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
    (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
    (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
    (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
    (7, 'Art', 94),
    (9, 'Art', 92);

-- 5. Все оценки Alice Johnson
SELECT g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 6. Средний балл по каждому студенту
SELECT s.full_name, ROUND(AVG(g.grade),2) as avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id;

-- 7. Студенты, родившиеся после 2004 года
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 8. Все предметы и их средний балл
SELECT subject, ROUND(AVG(grade),2) as avg_grade
FROM grades
GROUP BY subject;

-- 9. Топ-3 студента с самым высоким средним баллом
SELECT s.full_name, ROUND(AVG(g.grade),2) as avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 3;

-- 10. Все студенты, получившие хотя бы одну оценку ниже 80
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;