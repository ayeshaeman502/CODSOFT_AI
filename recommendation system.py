class MovieRecommendationSystem:
    def __init__(self):
        # Sample movie data with genres (including some Indian movies)
        self.movies_data = {
            "Robot,Krrish,PK": ["Action", "Adventure", "Sci-Fi"],
            "Jab Tak Hai Jaan,DDLJ ,Veer-Zaara": ["Drama", "Romance"],
            "Mr. India,Kaal,Koi... Mil Gaya": ["Action", "Sci-Fi"],
            "Queen,Ludo,Andaz Apna Apna": ["Comedy", "Romance"],
            "Ludo,Andaz Apna Apna,Piku": ["Drama", "Comedy"],
            "Barfi,2 States,Kabhi Khushi Kabhie Gham": ["Drama", "Romance", "Bollywood"],
            "Kahaani,Drishyam,Andhadhun": ["Action", "Thriller", "Bollywood"]
        }

    def get_user_preferences(self):
        # Simulate user input for movie preferences
        print("Please enter your movie preferences (separated by commas):")
        user_preferences = input().split(',')
        return [preference.strip().capitalize() for preference in user_preferences]

    def recommend_movies(self, user_preferences):
        recommended_movies = []

        for movie, genres in self.movies_data.items():
            # Calculate the Jaccard similarity coefficient between user preferences and movie genres
            intersection = set(user_preferences) & set(genres)
            union = set(user_preferences) | set(genres)
            similarity_coefficient = len(intersection) / len(union)

            # Set a threshold for similarity (you can adjust this as needed)
            threshold = 0.3

            if similarity_coefficient > threshold:
                recommended_movies.append(movie)

        return recommended_movies

# Create an instance of the MovieRecommendationSystem
recommendation_system = MovieRecommendationSystem()

# Get user preferences
user_preferences = recommendation_system.get_user_preferences()

# Get and print recommended movies
recommended_movies = recommendation_system.recommend_movies(user_preferences)

if recommended_movies:
    print("Recommended Movies:", recommended_movies)
else:
    print("Sorry, no movies match your preferences.")
