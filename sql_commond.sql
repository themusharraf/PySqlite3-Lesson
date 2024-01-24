select * from users;

CREATE TABLE IF NOT EXISTS table_name (id PRIMARY KEY ,name VARCHAR(225));

drop table table_name;

INSERT INTO table_name (id, name) VALUES (1, 'salom');

SELECT id, name FROM table_name WHERE id == 1;



