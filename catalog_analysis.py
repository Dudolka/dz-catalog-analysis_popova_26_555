import math

# Исходные данные. Каталог фильмов

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Этап 1. Переменные, числа и модуль math


def average_rating(movies):
    """Возвращает средний рейтинг фильмов, округлённый до одного знака."""
    if not movies:
        return 0.0

    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает возраст старого, нового фильма и средний возраст."""
    if not movies:
        return (0, 0, 0)

    ages = [current_year - movie["year"] for movie in movies]

    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Переводит продолжительность фильма из минут в часы и минуты."""
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"


# Этап 2. Условия и оператор match


def rating_tier(rating):
    """Определяет категорию фильма по рейтингу."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Определяет категорию фильма по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы


def print_non_comedy_movies(movies):
    """Выводит названия фильмов, не относящихся к комедиям."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print(movie["title"])


def find_first_masterpiece(movies):
    """Находит первый фильм с рейтингом выше 9.0."""
    index = 0

    while index < len(movies):
        movie = movies[index]

        if movie["rating"] > 9.0:
            print("Первый шедевр:", movie["title"])
            break

        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее заданного порога."""
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count


# Этап 4. Строки


def normalize_title(title):
    """Приводит каждое слово названия к формату Title Case."""
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:].lower()
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)


def make_slug(title):
    """Преобразует название фильма в строку для URL."""
    normalized = normalize_title(title)
    return normalized.lower().replace(" ", "-")


def format_report_line(movie):
    """Формирует строку отчёта с информацией о фильме."""
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


# Запуск программы и проверка результатов


if __name__ == "__main__":
    # Проверка этапа 1
    print("Средний рейтинг:", average_rating(movies))
    print("Возраст фильмов:", catalog_age_stats(movies))
    print("Длительность 155 минут:", duration_in_hours(155))

    # Проверка этапа 2
    print("\nРейтинг 9.2:", rating_tier(9.2))
    print("Фильм 2024 года:", decade_label(2024))

    # Проверка этапа 3
    print("\nФильмы без жанра comedy:")
    print_non_comedy_movies(movies)

    print("\nПоиск первого шедевра:")
    find_first_masterpiece(movies)

    print("\nПроверка случая без шедевров:")
    movies_without_masterpieces = [movie for movie in movies if movie["rating"] <= 9.0]
    find_first_masterpiece(movies_without_masterpieces)

    print("\nКоличество фильмов длиннее 120 минут:", count_long_movies(movies))

    # Проверка этапа 4
    print("\nНормализация названия:", normalize_title("silent hours"))
    print("Slug:", make_slug("The Quiet Algorithm"))
    print("Строка отчёта:", format_report_line(movies[7]))
