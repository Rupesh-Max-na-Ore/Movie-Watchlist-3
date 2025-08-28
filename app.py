import datetime

import database

menu = """Please select one of the following options:
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
Your selection: """

WELCOME = "Welcome to the watchlist app!"

print(WELCOME)
database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    # Parse the entered release date string into a datetime object using the specified format
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    # Convert the datetime object to a POSIX timestamp (float, seconds since epoch)
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def prompt_watch_movie():
    # Show all users
    users = database.get_all_users()
    if users:
        print("Available users:")
        for user in users:
            print(f"- {user}")
    else:
        print("No users found. Please add a user first.")
        return

    # Show all movies
    movies = database.get_movies()
    if movies:
        print("Available movies:")
        for _id, title, release_date in movies:
            print(f"{_id}: {title}")
    else:
        print("No movies found. Please add a movie first.")
        return

    username = input("Username: ")
    movie_id = input("Movie ID: ")

    # Validate user
    if username not in users:
        print(f"User '{username}' does not exist! Please add the user first.")
        return

    # Validate movie ID
    movie_ids = [str(_id) for _id, _, _ in movies]
    if movie_id not in movie_ids:
        print(f"Movie ID '{movie_id}' does not exist! Please enter a valid movie ID.")
        return

    review = input("Enter your review (optional): ")
    rating = input("Enter your rating out of 100 (optional): ")
    rating = int(rating) if rating.strip().isdigit() else None

    database.watch_movie(username, movie_id, review, rating)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)  # False is default
    if movies:
        print_movie_list("Watched", movies)
    else:
        print(f"{username} has watched no movies yet!")


def prompt_search_movies():
    search_term = input("Enter the partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print(f"No matching movies found for |{search_term}| !")


def prompt_plan_movie():
    users = database.get_all_users()
    if not users:
        print("No users found. Please add a user first.")
        return
    print("Available users:")
    for user in users:
        print(f"- {user}")

    movies = database.get_movies()
    if not movies:
        print("No movies found. Please add a movie first.")
        return
    print("Available movies:")
    for _id, title, release_date in movies:
        print(f"{_id}: {title}")

    username = input("Username: ")
    movie_id = input("Movie ID: ")

    if username not in users:
        print(f"User '{username}' does not exist! Please add the user first.")
        return

    movie_ids = [str(_id) for _id, _, _ in movies]
    if movie_id not in movie_ids:
        print(f"Movie ID '{movie_id}' does not exist! Please enter a valid movie ID.")
        return

    expectation = input("What are your expectations for this movie? (optional): ")
    database.plan_movie(username, movie_id, expectation)
    print(f"Movie ID {movie_id} planned for user '{username}'.")


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        _id, title, release_date = movie[:3]
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d, %Y")
        print(f"{_id}: {title} (on {human_date})")
        if len(movie) > 3:
            # For planned movies, expectation is at index 3
            expectation = movie[3] if heading == "Planned" else None
            review = movie[3] if heading != "Planned" else None
            rating = movie[4] if heading != "Planned" else None
            if expectation:
                print(f"   Expectation: {expectation}")
            if review:
                print(f"   Review: {review}")
            if rating is not None:
                print(f"   Rating: {rating}/100")
    print("---- \n")


def prompt_show_planned_movies():
    username = input("Username: ")
    movies = database.get_planned_movies(username)
    if movies:
        print_movie_list("Planned", movies)
    else:
        print(f"{username} has no planned movies yet!")


def prompt_show_reviews_for_movie():
    movies = database.get_movies()
    if not movies:
        print("No movies found. Please add a movie first.")
        return
    print("Available movies:")
    for _id, title, release_date in movies:
        print(f"{_id}: {title}")
    movie_id = input("Enter the Movie ID to see all reviews: ")
    movie_ids = [str(_id) for _id, _, _ in movies]
    if movie_id not in movie_ids:
        print("Invalid Movie ID.")
        return
    reviews = database.get_reviews_for_movie(movie_id)
    if reviews:
        print(f"-- Reviews for movie ID {movie_id} --")
        for username, review, rating in reviews:
            print(f"User: {username}")
            if review:
                print(f"  Review: {review}")
            if rating is not None:
                print(f"  Rating: {rating}/100")
            print("----")
    else:
        print("No reviews or ratings found for this movie.")


while (user_input := input(menu)) != "11":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    elif user_input == "8":
        prompt_plan_movie()
    elif user_input == "9":
        prompt_show_planned_movies()
    elif user_input == "10":
        prompt_show_reviews_for_movie()
    else:
        print("Invalid input, please try again!")
