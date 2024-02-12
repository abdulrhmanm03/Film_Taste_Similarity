import numpy as np
from numpy.linalg import norm

def similarity(user1, user2, username1, username2):
    films1, films2 = (user1, user2) if len(user1) <= len(user2) else (user2, user1)

    vector1 = []
    vector2 = []
    E = 0
    for n in films1:
        if n in films2:
            vector1.append(films1[n])
            vector2.append(films2[n])
            E += abs(films1[n]-films2[n])
            
    if len(vector1) == 0:
        print('0 common rated film :(')
    else: 
        print('')       
        print(f'{len(vector1)} common rated film')
        print('') 
                    
        vector1, vector2 = np.array(vector1), np.array(vector2) 
             
        # Users consistently assigned higher ratings to good films and lower ratings to bad ones, resulting in high scores for everyone in the cosine similarity 
        # Used the square of both vectors to penalize the difference more
        # It creates a new vector and angle, yes, but I don't think that really matters in our case
        dot_product = np.dot((vector1**2), (vector2**2))
        norm_vector1, norm_vector2 = norm((vector1**2)), norm((vector2**2))
        cosine_similarity = dot_product / (norm_vector1 * norm_vector2)
        
        
        MSE = (1 - (E/((len(vector1)*10))))
        
        pearson_corr = np.corrcoef(vector1, vector2)[0, 1]
        normalized_pearson_corr = 0.5 * (pearson_corr + 1)
        
        print(f"similarity based on various metrics  between {username1} and {username2}")
        print("")
        print("Cosine Similarity: ", round(cosine_similarity, 3), "range from -1 to 1")
        print("---------------------------------------------------------------------------------")
        print("Normalized Pearson Correlation Coefficient: ", round(normalized_pearson_corr, 3)*100, " from 0 to 100")
        print("---------------------------------------------------------------------------------")
        print("based on Mean squered error: ", round(MSE, 3)*100, " from 0 to 100")
        print("---------------------------------------------------------------------------------")
        print("")