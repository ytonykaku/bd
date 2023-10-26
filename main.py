import sqlite3 as sql3

def main():
    con = sql3.connect("teste.db")
    cur = con.cursor()
    cur.execute(team)