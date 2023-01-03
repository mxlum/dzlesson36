import cgi
import json

def loginScript():

    print("Content-Type: text/html")
    print()

    form = cgi.FieldStorage()
    with open("users.json") as file:
        users = json.load(file)
        if "userlogin" not in form or "userpassword" not in form:
            print("<H1>Error</H1>")
            print("Заполните все поля ввода")
        elif not form['userlogin'] in users.keys():
            print("<h1>Error</h1>")
            print("Пользователя с таким логином не сущевствует")
        elif form['userpassword'] != users[form["userlogin"]]:
            print("<h1>Error</h1>")
            print("Неверный пароль")
        else:
            print("<h1>Вы успешно вошли</h1>")

loginScript()
