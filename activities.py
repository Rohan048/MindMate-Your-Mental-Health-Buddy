def get_suggestion(mood):
    suggestions = {
        'Happy': "Great! Keep a gratitude journal today.",
        'Sad': "Try writing down your feelings or go for a short walk.",
        'Angry': "Do 3 minutes of deep breathing.",
        'Anxious': "Try a 5-minute mindfulness meditation.",
        'Calm': "Reflect and write a few things you're thankful for.",
        'Alone': "Watch Favourite movies & Series "
    }
    return suggestions.get(mood, "Take a deep breath and relax.")
