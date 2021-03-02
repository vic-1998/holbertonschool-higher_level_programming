 -- creates the TABLE id_not_null ON your MySQL server.
--  ID can't be null
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1, 
    name VARCHAR(256)
);
