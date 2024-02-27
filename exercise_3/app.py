from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

orgs = ["Coding club", "Math club", "Sports club", "Book club", "Music club"]
registered_users = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        registered_users[name] = organization
        return redirect('/registered_users')
    return render_template('home.html', organizations=orgs)


@app.route('/registered_users')
def registered_users_list():
    return render_template('registered_users.html', users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)