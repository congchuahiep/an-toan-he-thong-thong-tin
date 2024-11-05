# Chạy chương trình

### Tạo môi trường

Create a project folder and a `.venv` folder within:

```bash
mkdir myproject
cd myproject
py -3 -m venv .venv
```

### Kích hoạt môi trường

Before you work on your project, activate the corresponding environment:

```bash
.venv\Scripts\activate
```

### Cài đặt Flask

Within the activated environment, use the following command to install Flask:

```bash
pip install Flask
```

### Chạy ứng dụng

To run the application, use the `flask` command or `python -m flask`. You need to tell the Flask where your application is with the `--app` option.

```bash
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Chương trình sẽ được chạy tại đường dẫn http://127.0.0.1:5000/

If another program is already using port 5000, you’ll see `OSError: [Errno 98]` or `OSError: [WinError 10013]` when the server tries to start
