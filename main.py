from fastapi import FastAPI, Form,File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import sqlite3
#python -m uvicorn main:app --reload

app = FastAPI()
tem= Jinja2Templates(directory=".")
app.mount("/style", StaticFiles(directory="style"), name="style")

def ceak(n,p):
    conn=sqlite3.connect("data.db")
    con=conn.cursor()
    con.execute("select * from d where name=? and password=?",(n,p))
    data=con.fetchall()
    conn.close()
    return data

def add_new(n,p):
    conn=sqlite3.connect("data.db")
    con=conn.cursor()
    con.execute("INSERT INTO d (name, password) VALUES (?, ?)", (n,p))
    conn.commit()
    conn.close()
    d="all/"+n+".txt"
    with open(d,"w") as f:
        f.write(f"hello,\n{n}")
    return f"your account add name={n}"

def all_text(n):
    file=os.listdir("all")
    for i in file:
        f=n+".txt"
        if i==f:
            rr="all/"+f
            with open(rr , "r") as q:
                read=q.read()
                return read

def re_write(n,m):
    name="all/"+n+".txt"
    with open(name,"w") as f:
        f.write(m)
        return "save succfull"

@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
async def home(request:Request ):
    return tem.TemplateResponse(
        request=request,
        name="template/index1.html",
        context={
            "n":"(: welcome :)"
        }
    )

@app.post("/login" , response_class=HTMLResponse)
def login_to(request:Request , user_name:str=Form(...),password:str=Form(...)):
    read=all_text(user_name)
    data=ceak(user_name,password)
    if data:
        if user_name==data[0][0] and password==data[0][1]:
            return tem.TemplateResponse(
                request=request,
                name="template/index2.html",
                context={
                    "p":user_name,
                    "pp":password,
                    "n":user_name,
                    "r":read
                }
            )
        else:
           return tem.TemplateResponse(
                request=request,
                name="template/index1.html",
                context={
                    "n":"passeord or name wonrg"
                }
            )
    else:
        return tem.TemplateResponse(
            request=request,
            name="template/index1.html",
            context={
                "n":"no account found"
            }
        )

@app.post("/read",response_class=HTMLResponse)
def save_data(request:Request,p:str=Form(...), da:str=Form(...)):
    d=re_write(p,da)
    a=all_text(p)
    return tem.TemplateResponse(
        request=request,
        name="template/index2.html",
        context={
            "n":p,
            "p":p,
            "da":a,
            "m":d,
            "r":a
        }
    )

@app.get("/go",response_class=HTMLResponse)
def new_go(request:Request):
    return tem.TemplateResponse(
        request=request,
        name="template/index3.html"
    )

@app.post("/new" , response_class=HTMLResponse)
def newaccount(request:Request,new_user_name:str=Form(...), new_password:str=Form(...)):
    a=add_new(new_user_name,new_password)
    return tem.TemplateResponse(
        request=request,
        name="template/index1.html",
        context={
            "n":a
        }
    )
