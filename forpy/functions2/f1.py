movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# def check_movie_rating(movie_name):
#     for movie in movies:
#         if movie["name"].lower() == movie.name.lower():
#             if movie["imdb"]>5.5:
#                 return f"{movie_name} has imdb higher than 5.5"
#             else:
#                 return f"{movie_name} has imdb lower than 5.5"
#     return "Movie not found in the database"

# def high_rated(movie):
#     return movie["imdb"]>5.5

# for movie in movies:
#     print(f"{movie['name']}: {high_rated(movie)}")


# def check_category(category):
#     category_movies=[movie["name"] for movie in movies if movie["category"].lower() == category.lower()]

#     if category_movies:
#         return f"Movies in '{category}' category:\n"+ "\n".join(category_movies)
#     else:
#         return f"No movies found in this category"
# category = input()
# print(check_category(category))

def average_imdb(movies):
    if not movies:
        return "No movies in the list."
    total = sum(movie["imdb"] for movie in movies)
    return round(total/len(movies), 2)

# print(average_imdb(movies))

def check_category(category):
    return [movie for  movie in movies if movie["category"].lower()== category.lower()]

categorynew=input()
category_imdb = check_category(categorynew)
print(average_imdb(category_imdb))
