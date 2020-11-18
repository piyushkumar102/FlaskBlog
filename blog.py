from flask import Flask, redirect, render_template, url_for, flash, redirect

from form import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '6a160c417ee87e0ca81e05730c654db4'
posts = [
    {
        'auth': 'Piyush Kumar',
        'title': 'Blog 1',
        'content': 'Init',
        'date': '17 November 2020'
    },
    {
        'auth': 'Kumar',
        'title': 'Blog 2',
        'content': 'Second',
        'date': '17 November 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('Login in Success', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
