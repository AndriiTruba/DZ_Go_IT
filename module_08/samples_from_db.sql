-- 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.name_student, round(AVG(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.id_student
GROUP BY s.name_student
ORDER BY avg_grade DESC
LIMIT 5;


-- 1 студент із найвищим середнім балом з одного предмета.
SELECT d.name_discipline, s.name_student, round(AVG(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN disciplines d ON d.id = g.id_discipline
WHERE d.id = 1
GROUP BY s.name_student, d.name_discipline
ORDER BY avg_grade DESC
LIMIT 1;


-- Середній бал в групі по одному предмету.
SELECT d.name_discipline, gr.name_group , round(AVG(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN disciplines d ON d.id = g.id_discipline
LEFT JOIN [groups] gr ON gr.id = s.id_group
WHERE d.id = 2
GROUP BY gr.name_group, d.name_discipline
ORDER BY avg_grade DESC;


-- Середній бал у потоці.
SELECT round(AVG(g.grade), 2) AS avg_grade
FROM grades g;


-- Які курси читає викладач.
SELECT t.name_teacher, d.name_discipline
FROM teachers t
LEFT JOIN  disciplines d  ON t.id = d.id_teacher
WHERE t.id = 2;


-- Список студентів у групі.
SELECT s.name_student, gr.name_group
FROM students s
LEFT JOIN [groups] gr ON gr.id = s.id_group
WHERE gr.id = 1


-- Оцінки студентів у групі з предмета.
SELECT d.name_discipline, gr.name_group, s.name_student, g.grade, g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN disciplines d ON d.id = g.id_discipline
LEFT JOIN [groups] gr ON gr.id = s.id_group
WHERE d.id = 2 AND gr.id = 3;


-- Оцінки студентів у групі з предмета на останньому занятті.
SELECT d.name_discipline, gr.name_group, s.name_student, g.grade, g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN disciplines d ON d.id = g.id_discipline
LEFT JOIN [groups] gr ON gr.id = s.id_group
WHERE d.id = 4 AND gr.id = 1 AND g.date_of = (SELECT g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN [groups] gr ON gr.id = s.id_group
WHERE d.id = 4 AND gr.id = 1
ORDER BY g.date_of DESC);


-- Список курсів, які відвідує студент.
SELECT s.name_student, d.name_discipline
FROM grades g
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN disciplines d ON d.id = g.id_discipline
WHERE s.id = 1
GROUP BY d.name_discipline;


-- Список курсів, які студенту читає викладач.
SELECT t.name_teacher, s.name_student, d.name_discipline
FROM grades g
LEFT JOIN  teachers t  ON t.id = d.id_teacher
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN disciplines d ON d.id = g.id_discipline
WHERE t.id = 2 AND g.id_student = 1
GROUP BY d.name_discipline;


-- Середній бал, який викладач ставить студенту.
SELECT t.name_teacher, s.name_student, round(AVG(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN  teachers t  ON t.id = d.id_teacher
LEFT JOIN students s ON s.id = g.id_student
LEFT JOIN disciplines d ON d.id = g.id_discipline
WHERE t.id = 2 AND s.id = 3
GROUP BY s.name_student;


-- Середній бал, який ставить викладач.
SELECT t.name_teacher, round(AVG(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN  teachers t  ON t.id = d.id_teacher
LEFT JOIN disciplines d ON d.id = g.id_discipline
WHERE t.id = 3
GROUP BY t.name_teacher;