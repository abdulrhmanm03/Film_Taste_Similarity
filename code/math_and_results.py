import numpy as np
from numpy.linalg import norm

def similarity(user1_data, user2_data):
    films1, films2 = (user1_data, user2_data) if len(user1_data) <= len(user2_data) else (user2_data, user1_data)

    vector1 = []
    vector2 = []
    E = 0
    for n in films1:
        if n in films2:
            vector1.append(films1[n])
            vector2.append(films2[n])
            E += abs(films1[n]-films2[n])
            
    if len(vector1) == 0:
        return {'common_rated_film': 0}
    
       
    common_rated_film =len(vector1)
                
    vector1, vector2 = np.array(vector1), np.array(vector2) 
            
    # Users consistently assigned higher ratings to good films and lower ratings to bad ones, resulting in high scores for everyone in the cosine similarity 
    # Used the square of both vectors to penalize the difference more
    # It creates a new vector and angle, yes, but I don't think that really matters in our case
    dot_product = np.dot((vector1**2), (vector2**2))
    norm_vector1, norm_vector2 = norm((vector1**2)), norm((vector2**2))
    cosine_similarity = round(dot_product / (norm_vector1 * norm_vector2), 2)
    
    
    MAE = round((1 - (E/((len(vector1)*10)))), 2)
    
    pearson_corr = round(np.corrcoef(vector1, vector2)[0, 1], 2)

    return {'common_rated_film': common_rated_film,
            'cosine_similarity': cosine_similarity, 
            'pearson_corr': pearson_corr, 
            'MAE': MAE}
    