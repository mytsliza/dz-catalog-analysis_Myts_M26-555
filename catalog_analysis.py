import math

# --- ИСХОДНЫЕ ДАННЫЕ ---
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# --- ЭТАП 1 ---
def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округленную до одного знака."""
    if not movies:
        return 0.0
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый фильм в годах, самый новый, среднее)."""
    if not movies:
        return (0, 0, 0)

    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    avg_age = sum(ages) / len(ages)

    return (oldest, newest, math.ceil(avg_age))


def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# --- ЭТАП 2 ---
def rating_tier(rating):
    """Возвращает категорию по оценке, используя тернарный оператор."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        # Тернарный оператор
        return "средне" if rating < 6.9 else "средне"
    else:
        return "слабо"


def decade_label(year):
    """Возвращает метку десятилетия через match-case."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# --- ЭТАП 3 ---
def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold минут."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def print_non_comedy(movies):
    """Выводит названия фильмов, которые НЕ комедии (с использованием continue)."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue  # Пропускаем комедии
        print(movie["title"])


def find_first_masterpiece(movies):
    """Ищет первый фильм с рейтингом > 9.0 (с использованием while и break)."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(f"Первый шедевр: {movies[index]['title']}")
            break
        index += 1
    else:
        # Ветка else выполняется, если цикл завершился без break
        print("Шедевров не найдено")

# --- ЭТАП 4 ---
def normalize_title(title):
    """Приводит строку к Title Case вручную, без str.title()."""
    words = title.split()
    result = []
    for word in words:
        # Делаем первую букву заглавной, остальные оставляем как есть
        normalized_word = word[0].upper() + word[1:]
        result.append(normalized_word)
    return " ".join(result)


def make_slug(title):
    """Превращает нормализованное название в слаг."""
    # Используем lower() и replace()
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    """Возвращает единую строку с описанием фильма."""
    # Сортируем жанры по алфавиту и склеиваем через запятую
    sorted_genres = ", ".join(sorted(movie["genres"]))
    
    # Вызываем функцию из Этапа 1 для перевода минут
    duration = duration_in_hours(movie["duration_min"])
    
    # Формируем строку через f-string
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: {sorted_genres}'
    )
# --- БЛОК ДЛЯ ПРОВЕРКИ ---
if __name__ == "__main__":
    print("--- ПРОВЕРКА ЭТАПА 1 ---")
    print(f"Средняя оценка: {average_rating(movies)}")
    print(f"Возраст фильмов: {catalog_age_stats(movies)}")
    print(f"155 минут это: {duration_in_hours(155)}")

    print("\n--- ПРОВЕРКА ЭТАПА 2 ---")
    print(f"Рейтинг 9.5: {rating_tier(9.5)}")
    print(f"Год 2018: {decade_label(2018)}")

    print("\n--- ПРОВЕРКА ЭТАПА 3 ---")
    print("Фильмы не-комедии:")
    print_non_comedy(movies)
    
    print(f"\nФильмов длиннее 120 минут: {count_long_movies(movies)}")
    
    print("\nПоиск шедевра:")
    find_first_masterpiece(movies)

    print("\n--- ПРОВЕРКА ЭТАПА 4 ---")
    print(f"normalize_title('silent hours'): {normalize_title('silent hours')}")
    print(f"make_slug('Silent Hours'): {make_slug('Silent Hours')}")
    print(f"Строка отчета: {format_report_line(movies[7])}")
