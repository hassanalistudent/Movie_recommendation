import streamlit as st
import pickle as pk
import helper

# movies
movie_detail_dataset = pk.load(open("imported from jupyter notebook/movies/detail_of_movie.pkl","rb"))
movie_dataset = pk.load(open("imported from jupyter notebook/movies/dataset.pkl","rb"))
movies_recommender = pk.load(open("imported from jupyter notebook/movies/movies_recommender.pkl","rb"))
# foods
foods_detail_dataset = pk.load(open("imported from jupyter notebook/foods/food_detail_dataset.pkl",'rb'))
foods_dataset = pk.load(open("imported from jupyter notebook/foods/new_dataset.pkl",'rb'))
foods_recommender = pk.load(open("imported from jupyter notebook/foods/similarity_recommender.pkl",'rb'))


st.sidebar.title("Content Based Recommendations Systems")
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-Z9L4NzGtOuLttslg6GxDr9uCWqQxAZm7iQ&usqp=CAU")
user_menu = st.sidebar.radio("Select Recommendation System:",("Movies Recommendations","Indian Foods Recommendations"))

# movies
if user_menu == "Movies Recommendations":
    st.title("Movies Recommendation System")
    movie_name = st.selectbox("Select Movie Name:", movie_dataset["title"].unique())
    movie_nos = st.sidebar.selectbox("How many movies?", [0,2,4,6,8])
    st.sidebar.header("Project Details:")
    st.sidebar.write("Details of this project are mentioned in my Github repository. Here is link 'https://github.com/AbdullahProjects/Content-Based-Recommendation-Systems'")
    st.sidebar.header("About Developer")
    st.sidebar.write("This project is developed by Abdullah Khan Kakar. Here is my linkedin profile: 'https://www.linkedin.com/in/abdullah-khan-kakar-51555129a/'")


    name,movie_poster,current_movie = helper.recommend(movie_dataset, movies_recommender, movie_name, movie_nos)
    if movie_nos==0:
        st.write("How many movies you want to know? Select from sidebar.")
    else:
        st.header("You search it:")
        st.write(current_movie[0])
        st.image(current_movie[1])

        st.header("Recommendations for you:")
        if int(movie_nos) == 2:
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(movie_poster[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(movie_poster[1])              
        
        if int(movie_nos) == 4:            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(movie_poster[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(movie_poster[1])
            col3, col4 = st.columns(2)
            with col3:
                st.write(f"{3}. "+name[2])
                st.image(movie_poster[2])
            with col4:
                st.write(f"{4}. "+name[3])
                st.image(movie_poster[3])

        if int(movie_nos) == 6:
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(movie_poster[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(movie_poster[1])
            col3, col4 = st.columns(2)
            with col3:
                st.write(f"{3}. "+name[2])
                st.image(movie_poster[2])
            with col4:
                st.write(f"{4}. "+name[3])
                st.image(movie_poster[3])
            col5, col6 = st.columns(2)
            with col5:
                st.write(f"{5}. "+name[4])
                st.image(movie_poster[4])
            with col6:
                st.write(f"{6}. "+name[5])
                st.image(movie_poster[5])

        if int(movie_nos) == 8:
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(movie_poster[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(movie_poster[1])
            col3, col4 = st.columns(2)
            with col3:
                st.write(f"{3}. "+name[2])
                st.image(movie_poster[2])
            with col4:
                st.write(f"{4}. "+name[3])
                st.image(movie_poster[3])
            col5, col6 = st.columns(2)
            with col5:
                st.write(f"{5}. "+name[4])
                st.image(movie_poster[4])
            with col6:
                st.write(f"{6}. "+name[5])
                st.image(movie_poster[5])
            col7, col8 = st.columns(2)
            with col7:
                st.write(f"{7}. "+name[6])
                st.image(movie_poster[6])
            with col8:
                st.write(f"{8}. "+name[7])
                st.image(movie_poster[7])

        name.insert(0, current_movie[0])
        st.header("Here You Can See Movie Details:")
        selected_movie_name = st.selectbox("Select movie:", name)
        if st.button("See details"):
            id,title,genres,cast,crew,overview = helper.recommend_details(movie_detail_dataset, selected_movie_name)
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**ID**: {id}")
            with col2:
                st.write(f"**Title**: {title}")

            if len(crew)==1:
                st.write(f"**Director:** {crew[0]}")

            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Genres:**")
                count=1
                for i in range(len(genres)):
                    st.write(f"**{count}.** {genres[i]}")
                    count+=1
            with col2:
                st.write("**Top 3 Cast:**")
                count=1
                for i in range(len(cast)):
                    st.write(f"**{count}.** {cast[i]}")
                    count+=1
            st.write(f"**Overview:** {overview}")

# foods
if user_menu == "Indian Foods Recommendations":
    st.title("Indian Foods Recommendation System")
    food_name = st.selectbox("Select Food Name:", foods_dataset["name"].unique())
    food_nos = st.sidebar.selectbox("How many foods?", [0,2,4,6,8])
    st.sidebar.header("Project Details:")
    st.sidebar.write("Details of this project are mentioned in my Github repository. Here is link 'https://github.com/AbdullahProjects/Content-Based-Recommendation-Systems'")
    st.sidebar.header("About Developer")
    st.sidebar.write("This project is developed by Abdullah Khan Kakar. Here is my linkedin profile: 'https://www.linkedin.com/in/abdullah-khan-kakar-51555129a/'")


    current_food, name, food_posters = helper.recommend_food(foods_dataset, foods_recommender, food_name, food_nos)
    if food_nos==0:
        st.write("How many foods you want to know? Select from sidebar.")
    else:
        st.header("You search it:")
        st.write(current_food[0])
        st.image(current_food[1])

        st.header("Recommendations for you:")
        if int(food_nos) == 2:
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(food_posters[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(food_posters[1])              
        
        if int(food_nos) == 4:            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(food_posters[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(food_posters[1])
            col3, col4 = st.columns(2)
            with col3:
                st.write(f"{3}. "+name[2])
                st.image(food_posters[2])
            with col4:
                st.write(f"{4}. "+name[3])
                st.image(food_posters[3])

        if int(food_nos) == 6:
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(food_posters[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(food_posters[1])
            col3, col4 = st.columns(2)
            with col3:
                st.write(f"{3}. "+name[2])
                st.image(food_posters[2])
            with col4:
                st.write(f"{4}. "+name[3])
                st.image(food_posters[3])
            col5, col6 = st.columns(2)
            with col5:
                st.write(f"{5}. "+name[4])
                st.image(food_posters[4])
            with col6:
                st.write(f"{6}. "+name[5])
                st.image(food_posters[5])

        if int(food_nos) == 8:
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{1}. "+name[0])
                st.image(food_posters[0])
            with col2:
                st.write(f"{2}. "+name[1])
                st.image(food_posters[1])
            col3, col4 = st.columns(2)
            with col3:
                st.write(f"{3}. "+name[2])
                st.image(food_posters[2])
            with col4:
                st.write(f"{4}. "+name[3])
                st.image(food_posters[3])
            col5, col6 = st.columns(2)
            with col5:
                st.write(f"{5}. "+name[4])
                st.image(food_posters[4])
            with col6:
                st.write(f"{6}. "+name[5])
                st.image(food_posters[5])
            col7, col8 = st.columns(2)
            with col7:
                st.write(f"{7}. "+name[6])
                st.image(food_posters[6])
            with col8:
                st.write(f"{8}. "+name[7])
                st.image(food_posters[7])

        name.insert(0, current_food[0])
        st.header("Here You Can See Foods Details and its Recipe:")
        selected_food_name = st.selectbox("Select food:", name)
        if st.button("See details"):
            name, image_url, description, cuisine, course, diet, prep_time, instructions = helper.recommend_food_details(foods_detail_dataset, selected_food_name)

            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Name**: {name}")
            with col2:
                st.write(f"**Cuisine**: {cuisine}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Course**: {course}")
            with col2:
                st.write(f"**Diet**: {diet}")

            st.write(f"**Image URL:** {image_url}")

            st.write(f"**Description:** {description}")
            
            st.write(f"**Preparation Time:** {prep_time}")
            
            st.write(f"**Recipe:** {instructions}")
