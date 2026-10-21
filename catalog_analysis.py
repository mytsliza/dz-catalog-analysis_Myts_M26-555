import math

# --- ИСХОДНЫЕ ДАННЫЕ ---
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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


# --- БЛОК ДЛЯ ПРОВЕРКИ ---
if __name__ == "__main__":
    print("--- ПРОВЕРКА ЭТАПА 1 ---")
    print(f"Средняя оценка: {average_rating(movies)}")
    
    stats = catalog_age_stats(movies)
    print(f"Возраст фильмов (старый, новый, средний): {stats}")
    
    print(f"155 минут это: {duration_in_hours(155)}")
    print(f"89 минут это: {duration_in_hours(89)}")

    print("\n--- ПРОВЕРКА ЭТАПА 2 ---")
    print(f"Рейтинг 9.5: {rating_tier(9.5)}")
    print(f"Рейтинг 8.0: {rating_tier(8.0)}")
    print(f"Рейтинг 5.0: {rating_tier(5.0)}")
    print(f"Рейтинг 4.0: {rating_tier(4.0)}")

    print(f"Год 2024: {decade_label(2024)}")
    print(f"Год 2018: {decade_label(2018)}")
    print(f"Год 2010: {decade_label(2010)}")
