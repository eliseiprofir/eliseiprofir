import json


def add_movie(all_movies: list[dict[str, str]]) -> list[dict[str, str]]:
    print("\nEnter the movie's information.", end=" ")
    while True:
        movie_add: str = input("\nHit enter to add movie or type 'stop' when you're done. ").lower()
        if movie_add != 'stop':
            name: str = input("Name: ").title()
            year: str = input("Year: ")
            genre: str = input("Genre: ").title()
            all_movies.append({
                "Name":  name,
                "Year":  year,
                "Genre": genre
            })
        else:
            print("–––––––––––––––––––––––––")
            break
    return all_movies


def delete_movie(all_movies: list[dict[str, str]]) -> list[dict[str, str]]:
    while True:
        print("")
        for movie in all_movies:
            print(f"Movie: {movie['Name']}, Year: {movie['Year']}, Genre: {movie['Genre']}")
        print("")
        movie_del: str = input("Enter the movie title you want to delete, or 'stop' when you're done: ")
        if movie_del != 'stop':
            for movie in all_movies:
                if movie_del.title() == movie['Name']:
                    all_movies.remove(movie)
                    break
        else:
            print("–––––––––––––––––––––––––")
            break
    return all_movies


def print_movie(movie: dict[str, str]) -> str:
    return f"Name: {movie['Name']}, Year: {movie['Year']}, Genre: {movie['Genre']}"


def view_movies(all_movies: list[dict[str, str]]) -> None:
    print("")
    for movie in all_movies:
        print(print_movie(movie))
    print("–––––––––––––––––––––––––")


def find_movies(all_movies: list[dict[str, str]]) -> None:
    found: list[dict[str, str]] = []
    while True:
        criteria: str = input("\nWhat CRITERIA do you want to use in search. "
                              "Name, year or genre? (type 'stop' when you're done) ").title()
        if criteria == 'Stop':
            break
        elif criteria not in ["Name", "Year", "Genre"]:
            print("Criteria not found")
        else:
            search_by: str = input(f"Enter the {criteria}: ").title()
            for movie in all_movies:
                if search_by == movie[criteria]:
                    found.append(movie)
    print("")
    print("All movies matching your criteria(s) are:")
    for movie in found:
        print(print_movie(movie))
    print("–––––––––––––––––––––––––")


def load_movie_collection(file: str) -> list[dict[str, str]]:
    try:
        with open(file, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return default values if the file doesn't exist or is empty/corrupted


def save_movie_collection(all_movies, file: str) -> None:
    with open(file, 'w') as file:
        json.dump(all_movies, file, indent=4)


def main() -> None:
    file = 'movie_collection.json'
    all_movies: list[dict[str, str]] = load_movie_collection(file)
    print("–––––––––––––––––––––––––")
    print("Welcome to my little program for managing a movie collection.\n")
    print("This is your current collection.\n")
    for movie in all_movies:
        print(print_movie(movie))
    while True:
        operation: str = input("\nChoose your OPERATION: 'add', 'delete', 'view', 'find'. "
                               "When you want to stop the program, type 'stop'. ").lower()
        if operation == 'add':
            all_movies = add_movie(all_movies)
        elif operation == 'view':
            view_movies(all_movies)
        elif operation == 'delete':
            all_movies = delete_movie(all_movies)
        elif operation == 'find':
            find_movies(all_movies)
        elif operation == 'stop':
            print("\nThis is your collection now.\n")
            for movie in all_movies:
                print(print_movie(movie))
            print("\nThank you for using my program! 😊")
            print("–––––––––––––––––––––––––")
            break
        else:
            print("Operation not found. Try again. ")
            print("–––––––––––––––––––––––––")
    save_movie_collection(all_movies, file)


if __name__ == "__main__":
    main()
