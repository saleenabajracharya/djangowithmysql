from django.shortcuts import render
from django.contrib.auth import authenticate,login
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def logaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="9863034062",database="authentication")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        user=authenticate(request,email=em,password=pwd)
        
        c="select * from users where email='{}' ".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"error.html")
        else:
            return render(request,"welcome.html")
        

    return render(request,"login.html")
# Create your views here.
