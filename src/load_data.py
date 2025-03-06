from pathlib import Path
import polars as pl

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
IMDB_DIR = BASE_DIR / 'data' / 'raw' / 'imdb'
MOVIELENS_DIR = BASE_DIR / 'data' / 'raw' / 'movie-lens'
TMDB_DIR = BASE_DIR / 'data' / 'raw' / 'tmdb'

# Load functions
def load_imdb_basics():
    return pl.read_csv(IMDB_DIR / 'title.basics.tsv', separator='\t', null_values='\\N')

def load_imdb_akas():
    return pl.read_csv(IMDB_DIR / 'title.akas.tsv', separator='\t', null_values='\\N')

def load_imdb_ratings():
    return pl.read_csv(IMDB_DIR / 'title.ratings.tsv', separator='\t', null_values='\\N')

def load_movielens_movies():
    return pl.read_csv(MOVIELENS_DIR / 'movies.csv')

def load_movielens_ratings():
    return pl.read_csv(MOVIELENS_DIR / 'ratings.csv')

def load_movielens_tags():
    return pl.read_csv(MOVIELENS_DIR / 'tags.csv')

def load_tmdb_movies():
    return pl.read_csv(TMDB_DIR / 'tmdb_5000_movies.csv')

def load_all_data():
    data = {
        "imdb_basics": load_imdb_basics(),
        "imdb_akas": load_imdb_akas(),
        "imdb_ratings": load_imdb_ratings(),
        "movielens_movies": load_movielens_movies(),
        "movielens_ratings": load_movielens_ratings(),
        "movielens_tags": load_movielens_tags(),
        "tmdb_movies": load_tmdb_movies()
    }
    return data

if __name__ == "__main__":
    all_data = load_all_data()
    for name, df in all_data.items():
        print(f"Loaded {name} with {df.shape[0]} rows and {df.shape[1]} columns")