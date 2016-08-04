import requests
import json
import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()
# Make some fresh tables using executescript()
cur.executescript('''

DROP TABLE IF EXISTS user; 

CREATE TABLE user (
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    email     TEXT,
    last_name TEXT,
    active    TEXT,
    tags    TEXT
);''')



url = 'https://sj.teambookapp.com/api/users?per_page=1000'
r = requests.get(url, headers={'Authorization': 'Token token=56e4d2697115a9bcda5c3b28e6076f3c'})
value= json.loads(r.text)

for row in value:

    user_id =  row['id']
    user_email = row['email']
    lastName = row ['last_name']
    active = row['active']
   

    #if user_id is None or user_email is None or lastName is None or active is None or tags is None:
        #continue
    print(user_id,user_email,lastName, active)

    cur.execute('''INSERT OR REPLACE INTO user
    (id, email, last_name, active) VALUES ( ?, ?, ?, ?)''', (user_id,user_email,lastName,active,))

    conn.commit()
conn.close()