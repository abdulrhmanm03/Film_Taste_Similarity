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
            E += (films1[n]-films2[n])**2
            
    if len(vector1) == 0:
        print('0 common rated film :(')
    else: 
        print('')       
        print(f'{len(vector1)} common rated film')
        print('') 
                    
        vector1, vector2 = np.array(vector1), np.array(vector2)      

        dot_product = np.dot(vector1, vector2)

        norm_vector1, norm_vector2 = norm(vector1), norm(vector2)
        
        
        MSE = (1 - (E/(len(vector1)*10)))
        cosine_similarity = dot_product / (norm_vector1 * norm_vector2)
        normalized_cosine_similarity = 0.5 * (cosine_similarity + 1)
        transformed_similarity = 1-(np.arccos(cosine_similarity))
        pearson_corr = np.corrcoef(vector1, vector2)[0, 1]
        normalized_pearson_corr = 0.5 * (pearson_corr + 1)
        
        print(f"similarity based on various matrices between {username1} and {username2}")
        print("")
        print("Transformed Cosine Similarity: ", round(transformed_similarity, 3)*100)
        print("---------------------------------------------------------------------------------")
        print("Normalized Cosine Similarity: ", round(normalized_cosine_similarity, 3)*100)
        print("---------------------------------------------------------------------------------")
        print("Normalized Pearson Correlation Coefficient: ", round(normalized_pearson_corr, 3)*100)
        print("---------------------------------------------------------------------------------")
        print("Mean squered error: ", round(MSE, 3)*100)
        print("---------------------------------------------------------------------------------")
        print("")