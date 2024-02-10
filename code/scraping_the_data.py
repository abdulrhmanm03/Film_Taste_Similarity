from bs4 import BeautifulSoup
import requests

ratings_map = {
        '½': 1,
        '★': 2,
        '★½': 3,
        '★★': 4,
        '★★½': 5,
        '★★★': 6,
        '★★★½': 7,
        '★★★★': 8,
        '★★★★½': 9,
        '★★★★★': 10
}

user = {}
def main(soup):
        poster_container = soup.find_all(class_ = 'poster-container')

        for film in poster_container:
            if film.find(class_="rating"):
                poster = film.find(class_='poster')
                film_id = poster.get('data-film-id')
                rating = film.find(class_="rating").text
                user[film_id] = ratings_map[rating]

def scrap(username, q):
    
    url = f'https://letterboxd.com/{username}/films/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(f"getting {username} data....")
    main(soup=soup)
    
    n = int(soup.find_all(class_ = "paginate-page")[-1].text)
    for i in range(2, n+1):
        
        url = f'https://letterboxd.com/{username}/films/page/{i}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        main(soup=soup)
        
    print(f"{username} done") 
       
    if not user:
        print("field to get data")
        q.put({1:1})  
    else:      
        q.put(user)