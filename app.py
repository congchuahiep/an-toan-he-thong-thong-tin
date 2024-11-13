from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html', user=session.get('username'))

@app.route('/intro')
def intro():
    return render_template('intro.html', user=session.get('username'))

@app.route('/achivement')
def achivement():
    return render_template('achivement.html', user=session.get('username'))

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', user=session.get('username'))

@app.route('/it')
def it():
    return render_template('it.html', user=session.get('username'))

@app.route('/graphic')
def graphic():
    return render_template('graphic.html', user=session.get('username'))

@app.route('/toeicspeak')
def toeicspeak():
    return render_template('toeicspeak.html', user=session.get('username'))

@app.route('/toeicskill')
def toeicskill():
    return render_template('toeicskill.html', user=session.get('username'))

@app.route('/courses')
def courses():
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Lấy danh sách khoá học của người dùng từ database
    user_courses = get_user_courses(session['username'])
    
    return render_template('courses.html', user=session.get('username'), user_courses=user_courses)
#đăng nhập ở đây
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        from models import User
        # Lấy tên username và password từ form
        username = request.form['username']
        password = request.form['password']
        # Truy vấn tài khoản người dùng từ database
        user = User.query.filter_by(username=username).first()

        # Kiểm tra mật khẩu (bằng việc băm mật khẩu) và tài khoản
        if user and bcrypt.check_password_hash(user.password, password):
            # Khi kiểm tra thành công, thêm người dùng vào Session của hệ thống
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('home'))
        else:
            flash('Tài khoản hoặc mật khẩu không hợp lệ', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')
#đăng kí ở đây

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        from models import User
        # Lấy tên username và password từ form
        username = request.form['username']
        password = request.form['password']

        # Kiểm tra xem người dùng đã tồn tại chưa
        if User.query.filter_by(username=username).first():
            flash('Tên người dùng đã tồn tại', 'warning')
            return redirect(url_for('signup'))

        # Băm mật khẩu ra
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Tạo tài khoản mới và thêm vào database
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Tài khoản mới đã được tạo! Xin vui lòng đăng nhập', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Bạn đã đăng xuất', 'info')
    return redirect(url_for('login'))

def get_user_courses(username):
    # Lấy danh sách khoá học của người dùng từ database
    # ...
    return {}

