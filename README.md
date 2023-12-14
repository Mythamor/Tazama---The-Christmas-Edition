# Tazama: A Christmas Edition
A Django movie recommendation web app with a perfectly curated list of the top-rated Christmas holiday movies 

> **For an interactive view of Tazama: A Christmas Edition**, visit https://xmas.tazama.tech

![Screenshot from 2023-12-14 11-24-57](https://github.com/Mythamor/Tazama-A_Christmas_Edition/assets/113252977/90516054-475a-458a-8496-070922a2bcc8)

## NLP Recommendation Engine
The movie recommender system is powered by a robust dataset containing over 3500 movies and their overviews, which were used to create tags. Leveraging the capabilities of Natural Language Processing (NLP) and employing cosine similarity, this engine provides users with personalized movie recommendations. Given the limited dataset, users can get movie recommendations based on a broader concept. Recommendations based on movie genres, release_year, or a theme.

[Recommendation Notebook](https://github.com/Mythamor/Tazama-A-Movie-Recommendation-Web-App/blob/main/recommendation_engine/Movie_Recommendation_System.ipynb)

## Installation

### 1. Create Virtual Environment
``` bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
``` bash
    pip install -r requirements.txt
```
## Usage

### 1. Run Migrations
``` bash
    python manage.py migrate
```

### 2. Start the Party
``` bash
    python manage.py runserver
```

## Deployment: 
> What's your next holiday watch? Visit [Tazama -  A Christmas Edition](https://xmas.tazama.tech) for a recommendation.

>> Tazama is deployed on a custom-configured Nginx and Gunicorn Linux server on Digital Ocean

> Author: [Mithamo Beth](https://www.mithamo.tech)
