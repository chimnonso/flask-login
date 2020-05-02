from myproject import db, app
from flask import render_template, redirect, request, flash, url_for
from myproject.forms import RegistrationForm, LoginForm
from myproject.models import User
from flask_login import login_required, login_user, logout_user


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/welcome')
@login_required
def welcome():
   return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
   logout_user()
   flash("You just logged out")
   return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
# @login_required
def login():
   flash('login page')
   form = LoginForm()
   if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      try:
         if user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully")
            next = request.args.get('next')
            if next == None or next[0] == '/':
               next = url_for('welcome')

            return redirect(next)
      except Exception as e:
         print(e)
         flash("Email has not yet been registerd")
      
      # if user is not None and user.check_password(form.password.data):
      #    login_user(user)
      #    flash("Logged in successfully")
      #    next = request.args.get('next')
      #    if next == None or next[0] == '/':
      #       next = url_for('welcome')

      #    return redirect(next)
   return render_template('login.html', form=form)




@app.route('/register', methods=['GET', 'POST'])
# @login_required
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      user = User(email=form.email.data, username=form.username.data, password=form.password.data)
      db.session.add(user)
      db.session.commit()
      flash('Thanks for registration')
      return redirect(url_for('login'))
   return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
