-- No table for a meeting
-- Creates a view that lists all students that have a score under 80
CREATE VIEW need_meeting AS
SELECT
    name
FROM
    students
WHERE
    score < 80
    AND (students.last_meeting IS NULL
        OR students.last_meeting < NOW() - INTERVAL 1 MONTH);