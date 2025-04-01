from flask import Flask, render_template, request

app = Flask(name)

data_list = []  # Data store karne ke liye ek list

@app.route('/', methods=['GET', 'POST']) def index(): if request.method == 'POST': name = request.form.get('name') email = request.form.get('email') message = request.form.get('message')

if name and email and message:
        data_list.append({'name': name, 'email': email, 'message': message})

return render_template('index.html', data=data_list)

if name == 'main': app.run(debug=True)

