
# 🎬 Movie Watchlist App (PostgreSQL + Python)

A command-line movie watchlist application built with **Python 3**, **PostgreSQL**, and **psycopg2**.  
It allows users to:

- Add movies with release dates
- View all or upcoming movies
- Add users
- Mark movies as watched, with optional reviews and ratings
- Plan to watch movies with expectations
- Search movies by title
- View reviews for a particular movie

The project uses environment variables (via `.env`) to securely manage database credentials.

---

## 🚀 Features

- PostgreSQL database with relational tables (`movies`, `users`, `watched`, `planned`)
- Support for reviews, ratings, and expectations
- Indexing on movie release timestamps for faster queries
- Secure environment variable handling with `python-dotenv`
- Interactive CLI menu

---

## 📂 Project Structure

```
movie-watchlist-3/
│── app.py              # CLI entrypoint
│── database.py         # Database connection + SQL queries
│── .env.example        # Example environment variables
│── requirements.txt    # Python dependencies
│── README.md           # Documentation

````

---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/Rupesh-Max-na-Ore/Movie-Watchlist-3
cd movie-watchlist-3
````

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Fill in your PostgreSQL details inside `.env`:

```
DB_NAME=moviesdb
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 5. Create database in PostgreSQL

Start `psql` as a PostgreSQL user:

```bash
psql -U postgres
```

Create the database:

```sql
CREATE DATABASE moviesdb;
```

### 6. Run the application

```bash
python app.py
```

---

## 🧑‍💻 Welcome Screen and Menu

```
Welcome to the watchlist app!
Please select one of the following options:
1) Add new movies.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Add user to the app.
7) Search movies.
8) Plan to watch a movie.
9) View planned movies.
10) See all reviews for a movie.
11) Exit.
Your selection: (Enter Your Selction From Menu Here)
```

---

## 🔑 Notes

* Never commit your `.env` file. Use `.env.example` for sharing configuration.
* Make sure PostgreSQL server is running before launching the app.
* If psycopg2 fails to connect, check your `pg_hba.conf` authentication settings.

---

## 📜 License

This project is for educational and personal use. Feel free to modify or extend it.

---
