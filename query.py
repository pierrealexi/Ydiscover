from flask import Flask, render_template
import sqlite3

def query(req):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute(req)
    data = cur.fetchall()
    con.close()
    return data


def queryLogin(username, password):
    datas = query("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return datas

def queryRegister(data):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    data = (data[0], data[1], data[2], data[3])
    cur.execute(f"INSERT INTO Users (nom,prenom,email,motdepasse) VALUES (?,?,?,?)", data)
    con.commit()
    cur.close()
    con.close()

