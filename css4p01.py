# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:57:54 2024

@author: Derick
"""

import pandas as pd
    
file = pd.read_csv("movie_dataset.csv")

# Question 1
print("\n_________________\nQuestion 1\n____________________\n")
print("Highest rated movie in the dataset:")
print(file.loc[file["Rating"] == file["Rating"].max()]["Title"])

# Question 2
print("\n_________________\nQuestion 2\n____________________\n")
print("Average revenue (in millions):")
print(file["Revenue (Millions)"].mean())

# Question 3
print("\n_________________\nQuestion 3\n____________________\n")
print("Average revenue (in millions) for movies from 2015 to 2017:")
print(file[file["Year"].between(2015, 2017, inclusive = "both")]["Revenue (Millions)"].mean())

# Question 4
print("\n_________________\nQuestion 4\n____________________\n")
print("Number of movies released in the year 2016:")
print(len(file.loc[file["Year"] == 2016].index))

# Question 5
print("\n_________________\nQuestion 5\n____________________\n")
chris_nolan = file[file["Director"] == "Christopher Nolan"]
print("Number of movies directed by Christopher Nolan:")
print(len(chris_nolan.index))

# Question 6
print("\n_________________\nQuestion 6\n____________________\n")
print("Number of movies with a rating of at least 8.0:")
print(len(file.loc[file["Rating"] >= 8.0].index))

# Question 7
print("\n_________________\nQuestion 7\n____________________\n")
print("Median rating of Christopher Nolan's movies:")
print(chris_nolan["Rating"].median())

# Question 8
print("\n_________________\nQuestion 8\n____________________\n")
print("Year with the highest average rating:")
grouped = file.groupby("Year")["Rating"].mean().reset_index()
print(grouped.loc[grouped["Rating"].max() == grouped["Rating"]]["Year"])

# Question 9
print("\n_________________\nQuestion 9\n____________________\n")
print("Percentage increase in number of movies made between 2006 and 2016:")
grouped = file.groupby("Year")["Title"].count().reset_index()
initial_value = len(file.loc[file["Year"] == 2006].index)
final_value = len(file.loc[file["Year"] == 2016].index)
print(((final_value - initial_value)/initial_value) * 100)

# Question 10
print("\n_________________\nQuestion 10\n____________________\n")
print("Most common actor in all movies:")

file["Actors"] = file["Actors"].str.split(", ")
file = file.explode("Actors")
grouped = file.groupby("Actors").count().reset_index();
print(grouped.loc[grouped["Rank"].max() == grouped["Rank"]]["Actors"])

# Question 11
print("\n_________________\nQuestion 11\n____________________\n")
print("Number of unique genres:")

file["Genre"] = file["Genre"].str.split(",")
file = file.explode("Genre")
grouped = file.groupby("Genre").count().reset_index();
print(len(grouped.index))

# Question 12
print("\n_________________\nQuestion 12\n____________________\n")
file = pd.read_csv("movie_dataset.csv")
file.drop(columns=["Title", "Genre", "Description", "Director", "Actors"], inplace=True)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
print(file.corr())
