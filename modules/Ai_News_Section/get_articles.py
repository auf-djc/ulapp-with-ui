import pandas as pd
import joblib
from datetime import datetime, timedelta

def get_articles():
    # Load the trained model
    model = joblib.load('modules\Ai_News_Section\weather_classifier_model.joblib')

    # Load the articles to be classified
    articles_df = pd.read_excel('modules\Ai_News_Section\\articles\\articles.xlsx')

    # Convert the 'Date' column to datetime format
    articles_df['Date'] = pd.to_datetime(articles_df['Date'], errors='coerce')

    # Filter articles from the last 7 days to the present
    seven_days_ago = datetime.now() - timedelta(days=7)
    filtered_articles_df = articles_df[articles_df['Date'] >= seven_days_ago]

    # Make predictions for the filtered articles
    predictions = model.predict(filtered_articles_df['Title'])

    # Add the predicted ratings to the dataframe using .loc[]
    filtered_articles_df.loc[:, 'Predicted_Rating'] = predictions

    # Sort the dataframe by predicted rating in descending order
    filtered_articles_df = filtered_articles_df.sort_values(by='Predicted_Rating', ascending=False)

    # Get a maximum of 5 articles
    top_articles_count = min(5, len(filtered_articles_df))
    top_articles = filtered_articles_df.head(top_articles_count)

    # Extract titles
    titles = top_articles['Title'].tolist()

    return titles
