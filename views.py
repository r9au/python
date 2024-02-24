from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

'''def route(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())'''

#import mysql.connector
import mysql.connector

def validate_url(url):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="legion090903",
        database="website"
    )
    mycu = mydb.cursor()

    def end(s):
        l = s.split(".")
        x = l[-1]
        d = x[:4]
        if d == "com/":
            return True
        else:
            #print(f"Warning!!! website seems to be Malicious\n Note- Check for end of Domain \'.com\' is not present ")
            return False

    def indata(s):
        try:
            sql = "select exists(select 1 from domain where dname=%s)"  # it returns boolean value
            mycu.execute(sql, (s,))
            res = mycu.fetchone()[0]  # gives boolean value as output
            if not res:
                sq = "insert into domain (dname) values (%s)"
                mycu.execute(sq, (s,))
                mydb.commit()
                return False
            else:
                return True
        except mysql.connector.Error as err:
            print("Error !", err)

    l = 60
    s1 = "https://"
    l1 = url[8:].split("/")
    l1.append(url[:8])
    s = l1[0]
    lt = len(s)
    x = len(l1)
    y = url[:8]
    t = 0
    v = end(url)
    if not v:
        w0=f"""Warning!!! website seems to be Malicious\n 
        Note- Check for end of Domain \'.com\' is not present """
        return w0
    for i in s:
        if i not in "!@#$%^&*()=":
            continue
        else:
            t += 1
    if t == 0:
        if x <= 60 and y == s1 and v:
            w1=f"""The webesite is secured
             Note!!-Always check for \'{s1}\' label"""
            return w1
            da = indata(s)
            if da:
                return
            else:
                w2="Warning !! domain name not recorded seems to be Suspicious"
                return w2
        elif x >= 60:
            w3="Warning!! chances of threat the website lenghth is not standard"
            return w3
        elif y != s1:
            w4="Warning!! Potential threat the website doesnt have \'https\' label"
            return w4
    else:
        w5="""Warning!! Domain Name seems to be malicious
            Check Domain name it consists of characters:\'!@#$%^&*()=\'\nNot Recommended to access such site"""
        return w5

    mycu.close()
    mydb.close()

url=input("Enter the url:")
x=validate_url(url)
print(x)

# Create your views here.
#from django.shortcuts import render
#from django.http import HttpResponse

def cyber(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def action(request):
    if request.method=="POST":
        #x=validate_url(urx)
        return render(request,'validate_url')

