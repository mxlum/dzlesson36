import cgi
import json

def regScript():

    print("Content-Type: text/html")
    print()

    form = cgi.FieldStorage()
    with open("users.json") as file:
        users = json.load(file)
        if "newlogin" not in form or "newpassword" not in form:
            print("<H1>Error</H1>")
            print("Заполните все поля ввода")
        elif form["newlogin"].value in users.keys():
            print("<h1>Error</h1>")
            print("Логин уже используется")
        else:
            file.write(f"{form['newlogin'].value},{form['newpassword'].value}\n")
            users[form["newlogin"]] = form["newpassword"]
            json.dump(users, file)
            print("<h1>Вы успешно зарегистрированы!</h1>")

regScript()
