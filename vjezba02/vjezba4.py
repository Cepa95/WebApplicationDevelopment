import cgi
import cgitb
cgitb.enable(display=0, logdir="")
form = cgi.FieldStorage()

address = form.getvalue("email")

def check_email(address):
        if ("@" not in address):
           print("Location: vjezba2.py")
        divide=address.split("@")
        if (len(divide) !=2):
             print("Location: vjezba2.py")
        if (divide[1] !="unist.hr" or divide[1]!="oss.unist.hr"):
            print("Location: vjezba2.py")
        if (not divide[0].islower()):
            print("Location: vjezba2.py")

check_email(address)

