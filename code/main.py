from scraping_the_data import scrap
import multiprocessing
import numpy as np
from numpy.linalg import norm


def main():
    username1 = input("enter letterboxed username:  ")
    username2 = input("enter letterboxed username:  ")
    
    result_queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=scrap, args=(username1, result_queue))
    process2 = multiprocessing.Process(target=scrap, args=(username2, result_queue))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    
    user1 = result_queue.get()
    user2 = result_queue.get()
    
    
    films1, films2 = (user1, user2) if len(user1) <= len(user2) else (user2, user1)

    vector1 = []
    vector2 = []
    for n in films1:
        if n in films2:
            vector1.append(films1[n])
            vector2.append(films2[n])
            
    if len(vector1) == 0:
        print('0 common rated film')
    else:        
        print(len(vector1) + ' common rated film') 
                   
        vector1, vector2 = np.array(vector1), np.array(vector2)      

        dot_product = np.dot(vector1, vector2)

        norm_vector1, norm_vector2 = norm(vector1), norm(vector2)

        cosine_similarity = dot_product / (norm_vector1 * norm_vector2)
        normalized_cosine_similarity = 0.5 * (cosine_similarity + 1)
        transformed_similarity = 1-(np.arccos(cosine_similarity))
        pearson_corr = np.corrcoef(vector1, vector2)[0, 1]
        normalized_pearson_corr = 0.5 * (pearson_corr + 1)


        print("Transformed Similarity:", transformed_similarity*100)
        print("Normalized Cosine Similarity:", normalized_cosine_similarity*100)
        print("Normalized Pearson Correlation Coefficient:", normalized_pearson_corr*100)

if __name__ == "__main__":
    main()