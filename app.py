import streamlit as st
import pickle
import pandas as pd

backgroundColor = "black"

movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_detail = pickle.load(open('moviesdetail_dict.pkl', 'rb'))
movies_dataframe = pd.DataFrame(movies_detail)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


def overview(mov):
    over = movies_dataframe[movies_dataframe['title'].isin(mov)]
    index = over.index
    overview = []
    for i in index:
        overview.append(movies_dataframe.iloc[i].overview)

    return overview


def gen(mov):
    gen_ = movies_dataframe[movies_dataframe['title'].isin(mov)]
    index = gen_.index
    genr = []
    for i in index:
        genr.append(movies_dataframe.iloc[i].genres)

    return genr


def director(mov):
    dir = movies_dataframe[movies_dataframe['title'].isin(mov)]
    index = dir.index
    dirt = []
    for i in index:
        dirt.append(movies_dataframe.iloc[i].crew)

    return dirt


def cast(mov):
    cas = movies_dataframe[movies_dataframe['title'].isin(mov)]
    index = cas.index
    cast_ = []
    for i in index:
        cast_.append(movies_dataframe.iloc[i].cast)

    return cast_


st.title('MOVIE RECOMMENDER SYSTEM.')

selected_movie_name = st.selectbox(
    'PLEASE CHOOSE YOUR MOVIE.',
    movies['title'].values)

if st.button('RECOMMEND'):
    recomm = recommend(selected_movie_name)
    for i in recomm:
        st.write(i)

if st.sidebar.button('OVERVIEW'):
    recomm = recommend(selected_movie_name)
    over = overview(recomm)
    for i in range(len(recomm)):
        st.subheader(recomm[i].upper())
        st.write(over[i])

if st.sidebar.button("GENRES"):
    recomm = recommend(selected_movie_name)
    genr = gen(recomm)
    for i in range(len(recomm)):
        st.subheader(recomm[i].upper())
        for j in genr[i]:
            st.write(j)

if st.sidebar.button("DIRECTOR"):
    recomm = recommend(selected_movie_name)
    dirt = director(recomm)
    for i in range(len(recomm)):
        st.subheader(recomm[i].upper())
        for j in dirt[i]:
            st.write(j)

if st.sidebar.button("CAST"):
    recomm = recommend(selected_movie_name)
    cas = cast(recomm)
    for i in range(len(recomm)):
        st.subheader(recomm[i].upper())
        for j in cas[i]:
            st.write(j)