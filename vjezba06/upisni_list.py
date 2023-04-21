#!python
import cgi
import db
import translate
import base

params=cgi.FieldStorage()
student_id=params.getvalue('id')

subjects = db.get_subjects()
data = db.get_upisni_list(student_id)

base.start_html()
translate.print_list_button(subjects, data)
base.end_html()