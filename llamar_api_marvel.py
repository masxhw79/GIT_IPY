import hashlib
import requests
import json
import sqlite3

def main_api():
    public = '1c8899ab25f924b957daf375fd8b4126'
    private = 'a6eb184efcfdda224c1b782d9bf005f33791e8e9'
    ts = '1'
    hash = hashlib.md5((ts + private + public).encode()).hexdigest()

    base = 'http://gateway.marvel.com/v1/public/'
    caracter = requests.get(base + 'characters',
                            params={'apikey': public, 'ts' : ts, 'hash' : hash, 'name':'thor'}).json()
    nombre = (caracter ['data']['results'][0]['name'])
    descripcion = (caracter ['data']['results'][0]['description'])


    con = sqlite3.connect("/home/ec2-user/api/bd")
    cursor =con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS MARVEL
                   (NOMBRE TEXT NOT NULL,
                    DESCRIPCION TEXT NOT NULL)''')
    cursor.execute('''INSERT INTO MARVEL (NOMBRE,DESCRIPCION) VALUES (?,?)''', (nombre,descripcion))
    con.commit()  
    cursor.execute('''SELECT * FROM MARVEL''')
    print(cursor.fetchall())
    con.close() 
 		

if __name__ == '__main__':
    main_api()
