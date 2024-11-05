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
    if 'username' in session:
        return render_template('index.html', user=session['username'])
    return render_template('index.html')

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
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Tài khoản hoặc mật khẩu không hợp lệ', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        from models import User
        # Lấy tên username và password từ form
        username = request.form['username']
        password = request.form['password']
        # Băm mật khẩu ra
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Kiểm tra xem người dùng đã tồn tại chưa
        if User.query.filter_by(username=username).first():
            flash('Tên người dùng đã tồn tại', 'warning')
            return redirect(url_for('signup'))

        # Tạo tài khoản mới và thêm vào database
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Tài khoản mới đã được tạo! Xin vui lòng đăng nhập', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')