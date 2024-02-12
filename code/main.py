from scraping_the_data import scrap
from math_and_results import similarity
import multiprocessing

def main():
    username1 = input("enter letterboxed username:  ")
    username2 = input("enter letterboxed username:  ")
    print('')
    
    result_queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=scrap, args=(username1, result_queue))
    process2 = multiprocessing.Process(target=scrap, args=(username2, result_queue))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    
    user1_data = result_queue.get()
    user2_data = result_queue.get()
    
    print("caluclating.....")
    
    similarity(user1_data, user2_data, username1, username2)

if __name__ == "__main__":
    main()