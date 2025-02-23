import requests

# here functions of : Movies Recemmendation System
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a716cbb7c501852c46cc1fccaf0784fe")
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"

def recommend(dataset, recommender,  movie, no):
    movie_index = dataset[dataset["title"] == movie].index[0]
    current_movie_id = dataset.iloc[movie_index][0]
    distances = recommender[movie_index]
    recommend_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:int(no)+1]
    movies_list = []
    movies_posters = []
    current_movie = [dataset.iloc[movie_index][1], fetch_poster(current_movie_id)]

    for i in recommend_movies:
        movies_id = dataset.iloc[i[0]][0]
        movies_list.append(dataset.iloc[i[0]][1])
        # fetch posters from api
        movies_posters.append(fetch_poster(movies_id))
    return movies_list,movies_posters,current_movie

def recommend_details(dataset, movie):
    movie_index = dataset[dataset["title"] == movie].index[0]
    # movie_id = dataset.iloc[movie_index][0]
    id = dataset.iloc[movie_index][0]
    title = dataset.iloc[movie_index][1]
    genres = dataset.iloc[movie_index][2]
    cast = dataset.iloc[movie_index][5]
    crew = dataset.iloc[movie_index][6]
    overview = dataset.iloc[movie_index][4]
    return id,title,genres,cast,crew,overview



# here functions of : Indian Foods Recemmendation System
def recommend_food(n_dataset, similarity_recommender, food_name, food_noc):
    
    food_index = n_dataset[n_dataset["name"] == food_name].index[0]
    distances = similarity_recommender[food_index]
    recommend_foods = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:int(food_noc)+1]
    current_food = [n_dataset.iloc[food_index][0], n_dataset.iloc[food_index][1]]
    food_list = []
    food_image = []
    for i in recommend_foods:
        index = i[0]
        food_list.append(n_dataset.iloc[index][0])
        food_image.append(n_dataset.iloc[index][1])

    return current_food, food_list, food_image


def recommend_food_details(dataset, food):
    food_index = dataset[dataset["name"] == food].index[0]
    name = dataset.iloc[food_index][0]
    image_url = dataset.iloc[food_index][1]
    description = dataset.iloc[food_index][2]
    cuisine = dataset.iloc[food_index][3]
    course = dataset.iloc[food_index][4]
    diet = dataset.iloc[food_index][5]
    prep_time = dataset.iloc[food_index][6]
    instructions = dataset.iloc[food_index][7]
    
    return name, image_url, description, cuisine, course, diet, prep_time, instructions