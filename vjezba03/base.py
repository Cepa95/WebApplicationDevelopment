#!python.exe

def start_html():
    print('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vjezba03</title>
    <style>
    table, th, tr, td {
        border: 1px solid
        }
    </style>
    </head>
    <body>
    <form method="post"> 
    ''')                ##ne treba action sada

def end_html():
    print('''
    </form>
    </body>
    </html>
    ''')