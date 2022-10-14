# :pill: django medic shop

Django medic shop is a medical-ecommerce site built using python and django.With most of the features like `user-auth`,`reviewing-product`,`placing-order` and many more.

## :bookmark_tabs: Contents

Being a `django` project ,taking advantage of the `MVT` architechture ,we are seperating our project into apps.

- [x] 👮 **base**
      This contains all the auth related stuff, like `authentication` , `creating-customers`.
- [x] 🛒 **cart**
      As the name describes it realted all the cart realted information like `coupons`,`cart` and `order-item`.
- [x] ⚕️ **products**
      This acts as a wrapper for the items in thw website mainly contain the information related to `items`.
- [x] **Store**
      This contains all the store realted stuff like `item-review`, `item`.

The apps seperation is very unlikely but really help in the process of development.

### :anchor: DataBase

For every `backend-based` app `database` is one of the most important thing. The app is configured for `sqlite` database but other databases like [postgres]("https://www.postgresql.org/") or [mysql]("https://www.mysql.com/") could be used. But for the development purpose we are using `sqlite` only. But for production purpose the configuration for `postgres` or `mysql` should be given like

### 🏇 Get Started

Clone this repository 🔂

```bash
    git clone <project-url>
    cd <project-name>
```

**requirements.txt** contains all the requirements for this project. It's adviced to install all the requirements in a `virtual-env`.

```bash
    pip install -r requirements.txt
```

Your are ready with your enviroment you can now run the development server. But first let's run our migrations .

```bash
    python manage.py migrate
```

This will apply all your migrations.
Being a `ecommerce-site` and not providing the `db` or `host-password-pair` for db, the products information too be loaded from a `*.json` file.

```bash
    python manage.py loaddata  products.json --appproducts
```

Now your products are added , 🚀 Lets run the `dev` server.

```bash
    python manage.py runserver
```

To run the server the server will provide a url head over to the website.

### 🧱 Conclusion

This is under construction for the mean time ,all the routes are checked ,further development of the project would occur if the front end demands.
