-- This command selects the scores and names from the `second_table` where the name is not NULL, ordered by score in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
