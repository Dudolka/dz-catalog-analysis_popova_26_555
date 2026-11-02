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
    """Возвращает средний рейтинг, округлённый до одного знака."""
    if not movies:
        return 0.0

    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает возраст старейшего, новейшего и средний возраст фильмов."""
    if not movies:
        return (0, 0, 0)

    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Переводит минуты в формат «2ч 35м»."""
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
    """Выводит первый фильм с рейтингом строго выше 9.0 или сообщение."""
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
    """Считает фильмы длиннее заданного порога в минутах."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Этап 4. Строки


def normalize_title(title):
    """Приводит название к Title Case без использования str.title()."""
    words = title.split()
    normalized_words = []
    for word in words:
        normalized_word = word[0].upper() + word[1:].lower()
        normalized_words.append(normalized_word)
    return " ".join(normalized_words)


def make_slug(title):
    """Преобразует название в строку вида the-quiet-algorithm."""
    normalized = normalize_title(title)
    return normalized.lower().replace(" ", "-")


def format_report_line(movie):
    """Формирует единую строку с описанием фильма."""
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


# Этап 5. Списки


def titles_sorted_by_rating(movies):
    """Возвращает названия фильмов по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Возвращает топ-N фильмов как список кортежей (название, рейтинг)."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# Этап 6. Словари


def count_by_genre(movies):
    """Подсчитывает фильмы каждого жанра через dict.get()."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Возвращает словарь актёров и списков их фильмов."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def movies_above_average(movies):
    """Создаёт словарь названий и рейтингов выше среднего рейтинга каталога."""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }


# Запуск программы и проверка этапов 1–6

if __name__ == "__main__":
    print("Средний рейтинг:", average_rating(movies))
    print("Возраст фильмов:", catalog_age_stats(movies))
    print("Длительность 155 минут:", duration_in_hours(155))

    print("\nРейтинг 9.2:", rating_tier(9.2))
    print("Фильм 2024 года:", decade_label(2024))

    print("\nФильмы без жанра comedy:")
    print_non_comedy_movies(movies)
    print("\nПоиск первого шедевра:")
    find_first_masterpiece(movies)
    print("\nПроверка случая без шедевров:")
    find_first_masterpiece([movie for movie in movies if movie["rating"] <= 9.0])
    print("\nКоличество фильмов длиннее 120 минут:", count_long_movies(movies))

    print("\nНормализация названия:", normalize_title("silent hours"))
    print("Slug:", make_slug("The Quiet Algorithm"))
    print("Строка отчёта:", format_report_line(movies[7]))

    print("\nНазвания фильмов по убыванию рейтинга:")
    for title in titles_sorted_by_rating(movies):
        print(title)
    print("\nТоп-3 фильма:")
    print(top_n_by_rating(movies))

    print("\nКоличество фильмов по жанрам:")
    for genre, count in sorted(count_by_genre(movies).items()):
        print(f"{genre}: {count}")

    print("\nФильмография актёров:")
    for actor, titles in sorted(actor_filmography(movies).items()):
        print(f"{actor}: {', '.join(titles)}")

    print("\nФильмы с рейтингом выше среднего:")
    print(movies_above_average(movies))
