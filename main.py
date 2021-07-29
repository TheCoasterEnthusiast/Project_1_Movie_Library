movies = []
genres = {
    "R": "Romance",
    "A": "Action",
    "D": "Documentary",
    "H": "Horror",
    "C": "Comedy"
}
search_criterias = {
    "T": "Title",
    "Y": "Year",
    "D": "Director",
    "G": "Genre"
}


def add_movie():
    title = input("What is the movie's title? ")
    year = input(f"What year was {title} released? ")
    director = input(f"Who directed {title}? ")
    genre_input = input(f"Is {title} a: Romance 'R', Action 'A', Documentary 'D', Horror 'H', or Comedy 'C'? ")

    while genre_input != "R" and genre_input != "A" and genre_input != "D" and genre_input != "H" and genre_input != "C":
        print("Input not recognized, please try again.")
        genre_input = input(f"Is {title} a: Romance 'R', Action 'A', Documentary 'D', Horror 'H', or Comedy 'C'? ")

    genre = genres[genre_input]

    movies.append(
        {"title": title,
         "year": int(year),
         "director": director,
         "genre": genre
        }
    )


def view_movies():
    for movie in movies:
        print_movie_info(movie)


def print_movie_info(movie):
    print(f"""
        Title: {movie["title"]}
        Year: {movie["year"]}
        Director: {movie["director"]}
        Genre: {movie["genre"]}
        """
    )


def search_movie():
    search_criteria_input = input("Would you like to search by: Title 'T', Year 'Y', Director 'D', or Genre 'G'? ")
    while search_criteria_input != "T" and search_criteria_input != "Y" and search_criteria_input != "D" and search_criteria_input != "G":
        print("Input not recognized, please try again.")
        search_criteria_input = input("Would you like to search by: Title 'T', Year 'Y', Director 'D', or Genre 'G'? ")

    if search_criteria_input == "G":
        search_keyword = input("Romance 'R', Action 'A', Documentary 'D', Horror 'H', or Comedy 'C'? ")
    else:
        search_keyword = input(f"Search by {search_criterias[search_criteria_input]}: ")

    for movie in movies:
        if search_criteria_input == "T" and search_keyword.lower() == movie["title"].lower():
            print_movie_info(movie)
        elif search_criteria_input == "Y" and int(search_keyword) == movie["year"]:
            print_movie_info(movie)
        elif search_criteria_input == "D" and search_keyword.lower() == movie["director"].lower():
            print_movie_info(movie)
        elif search_criteria_input == "G":
            genre = genres[search_keyword]
            if genre == movie["genre"]:
                print_movie_info(movie)

main_menu_options = {
    "A": add_movie,
    "V": view_movies,
    "S": search_movie
}

main_menu_input = input("Would you like to: Add a movie 'A', View all movies 'V', Search for a movie 'S' or Quit 'Q'? ")
while main_menu_input != "Q":
    run_function = main_menu_options[main_menu_input]
    run_function()
    if main_menu_input != 'A' and main_menu_input != "V" and main_menu_input != "S":
        print("Input not recognized, please try again.")
        main_menu_input = input("Would you like to: Add a movie 'A', View all movies 'V', or Quit 'Q'? ")
