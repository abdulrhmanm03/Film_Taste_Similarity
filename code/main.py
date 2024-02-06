from scraping_the_data import scrap
import multiprocessing
import numpy as np
from numpy.linalg import norm

if __name__ == "__main__":
    username1 = input("enter letterboxed username:  ")
    username2 = input("enter letterboxed username:  ")
    
    result_queue = multiprocessing.Queue()

    # Create two processes and pass the queue
    process1 = multiprocessing.Process(target=scrap, args=(username1, result_queue))
    process2 = multiprocessing.Process(target=scrap, args=(username2, result_queue))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    print(111111111111111)
    

    # Retrieve results from the queue
    user1 = result_queue.get()
    user2 = result_queue.get()
    
    
    
    list1, list2 = (user1, user2) if len(user1) <= len(user2) else (user2, user1)

    vector1 = []
    vector2 = []
    for n, r in list1.items():
        if n in list2:
            vector1.append(list1[n])
            vector2.append(list2[n])
            
    if len(vector1) == 0:
        print('0 common rated film')
    else:        
        print(len(vector1) + ' common rated film')            
        vector1, vector2 = np.array(vector1), np.array(vector2)      

        dot_product = np.dot(vector1, vector2)

        norm_vector1, norm_vector2 = norm(vector1), norm(vector2)

        cosine_similarity = dot_product / (norm_vector1 * norm_vector2)
        transformed_similarity = 1-(np.arccos(cosine_similarity))
        pearson_corr = np.corrcoef(vector1, vector2)[0, 1]
        normalized_pearson_corr = 0.5 * (pearson_corr + 1)


        print("Transformed Similarity:", transformed_similarity*100)
        print("Cosine Similarity:", cosine_similarity*100)
        print("Normalized Pearson Correlation Coefficient:", normalized_pearson_corr*100)
