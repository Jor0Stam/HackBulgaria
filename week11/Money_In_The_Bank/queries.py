# CLIENTS

update_sql = "UPDATE clients SET message = ? WHERE id = ?"

update_sql = "UPDATE clients SET password = ? WHERE id = ?"

insert_sql = "insert into clients (username, password) values (?, ?)"

select_query = '''SELECT id, username, balance, message, password
FROM clients
WHERE username = ? LIMIT 1'''

create_clients_table = '''
create table if not exists
clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    balance REAL DEFAULT 0,
    message TEXT)'''

# LOG

create_log_table = '''
create table if not exists
log(id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    log_time TEXT)'''

create_log = '''
INSERT
INTO LOG (username, log_time)
VALUES (?, ?)'''

count_logs = '''
SELECT COUNT(*)
FROM log
where username = ?'''
