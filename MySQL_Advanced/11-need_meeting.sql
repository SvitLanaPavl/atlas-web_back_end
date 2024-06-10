-- No table for a meeting
-- Creates a view that lists all students that have a score under 80
CREATE VIEW need_meeting AS
SELECT
    students.name
FROM
    students
JOIN
    scores ON students.id = scores.student_id
LEFT JOIN
    meetings ON students.id = meetings.student_id
WHERE
    scores.score < 80
    AND (meetings.last_meeting IS NULL
        OR meetings.last_meeting < NOW() - INTERVAL 1 MONTH);