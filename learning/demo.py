import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table1 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table1 (id, completed) VALUES (1, TRUE);')

connection.commit()

connection.close()
cursor.close()