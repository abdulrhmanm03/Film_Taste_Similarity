# Film Taste Similarity

Film Taste Similarity is a FastAPI-based web service that allows users to compare the film tastes of two Letterboxd users. It fetches data asynchronously for both usernames and calculates multiple similarity matrices such as Cosine Similarity, Mean Absolute Error (MAE), and Pearson Correlation. The mathematical calculations are performed using NumPy.

## Features

- Asynchronous data fetching using `asyncio`
- Similarity calculations including:
  - Cosine Similarity
  - Mean Absolute Error (MAE)
  - Pearson Correlation
- FastAPI for creating a robust and efficient web service

## To run localy

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/film-taste-similarity.git
   cd film-taste-similarity/code
   
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the server

   ```bash
   uvicorn main:app --reload
