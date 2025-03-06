import polars as pl
import os

# Define base paths
IMDB_PATH = os.path.join('..', 'data', 'raw', 'imdb')
MOVIELENS_PATH = os.path.join('..', 'data', 'raw', 'movie-lens')
TMDB_PATH = os.path.join('..', 'data', 'raw', 'tmdb')

# IMDb Loaders
def load_imdb_basics():
    return pl.read_csv(os.path.join(IMDB_PATH, 'title.basics.tsv'), separator='\t', null_values='\\N')

def load_imdb_akas():
    return pl.read_csv(os.path.join(IMDB_PATH, 'title.akas.tsv'), separator='\t', null_values='\\N')

def load_imdb_crew():
    return pl.read_csv(os.path.join(IMDB_PATH, 'title.crew.tsv'), separator='\t', null_values='\\N')

def load_imdb_episode():
    return pl.read_csv(os.path.join(IMDB_PATH, 'title.episode.tsv'), separator='\t', null_values='\\N')

def load_imdb_principals():
    return pl.read_csv(os.path.join(IMDB_PATH, 'title.principals.tsv'), separator='\t', null_values='\\N')

def load_imdb_ratings():
    return pl.read_csv(os.path.join(IMDB_PATH, 'title.ratings.tsv'), separator='\t', null_values='\\N')

def load_imdb_names():
    return pl.read_csv(os.path.join(IMDB_PATH, 'name.basics.tsv'), separator='\t', null_values='\\N')

# MovieLens Loaders (normal CSVs)
def load_movielens_movies():
    return pl.read_csv(os.path.join(MOVIELENS_PATH, 'movies.csv'))

def load_movielens_ratings():
    return pl.read_csv(os.path.join(MOVIELENS_PATH, 'ratings.csv'))

def load_movielens_tags():
    return pl.read_csv(os.path.join(MOVIELENS_PATH, 'tags.csv'))

def load_movielens_links():
    return pl.read_csv(os.path.join(MOVIELENS_PATH, 'links.csv'))

# TMDB Loader
def load_tmdb_movies():
    return pl.read_csv(os.path.join(TMDB_PATH, 'tmdb_2023.csv'))

# Wrapper to Load All
def load_all_data():
    return {
        "imdb_basics": load_imdb_basics(),
        "imdb_akas": load_imdb_akas(),
        "imdb_crew": load_imdb_crew(),
        "imdb_episode": load_imdb_episode(),
        "imdb_principals": load_imdb_principals(),
        "imdb_ratings": load_imdb_ratings(),
        "imdb_names": load_imdb_names(),
        "movielens_movies": load_movielens_movies(),
        "movielens_ratings": load_movielens_ratings(),
        "movielens_tags": load_movielens_tags(),
        "movielens_links": load_movielens_links(),
        "tmdb_movies": load_tmdb_movies(),
    }