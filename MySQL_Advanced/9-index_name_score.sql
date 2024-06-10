-- Optimize search and score
-- Creates an index on the table and the first letter of name and score
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score)