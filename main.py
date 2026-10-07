from fastapi import FastAPI
import psycopg
import os
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

DB_URL=os.getenv("DATABASE_URL")
s=('cse','ece','eee','mech','it')

def getstudents(table:str,branch:str):
    if branch not in s:
        return []
    else:
        branch=branch.upper()
        with psycopg.connect(DB_URL) as conn:
            with conn.cursor() as curr:
                curr.execute(f'SELECT * FROM {table} WHERE branch = \'{branch}\' ORDER BY cgpa DESC')
                return curr.fetchall()

@app.get("/cse")
def csestudents():
    arr=list()
    arr=getstudents("juniors","cse")
    return arr

@app.get("/ece")
def ecestudents():
    return getstudents("juniors","ece")

@app.get("/mech")
def mechstuds():
    return getstudents("juniors","mech")

@app.get("/it")
def itstuds():
    return getstudents("juniors","it")

@app.get("/eee")
def eeestuds():
    return getstudents("juniors","eee")

