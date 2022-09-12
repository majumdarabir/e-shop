# E-Medi-Shop

### :small_red_triangle: About

This project is a server site rendered website made used `django`,`python`,`jinja`.

### :bookmark_tabs: Contents

Being a `django ` project ,taking advantage of the `MVT` architechture ,we are seperating the website content into apps. For simplicity we created a single app:

- [x] store

### :anchor: DataBase

For every `backend-based` app `database` is one of the most important thing. The app is configured for `sqlite` database but other databases like [postgres]("https://www.postgresql.org/") or [mysql]("https://www.mysql.com/") could be used. But for the development purpose we are using `sqlite` only.

### 🏇 Get Started

Clone this repository 🔂

```bash
    git clone https://github.com/majumdarabir/e-shop
    cd <project-name>
```

To get the requirements for these project. It's adviced to use this project over a `virtualenv` or `venv`.

```bash
    pip install -r requirements.txt
```

```bash
    python manage.py migrate
```

To apply all the migrations

```bash
    python manage.py runserver
```

To run the server the server will provide a url head over to the website

### 🧱 Conclusion

This is under construction for the mean time ,all the routes are checked ,further development of the project would occur if the front end demands.
