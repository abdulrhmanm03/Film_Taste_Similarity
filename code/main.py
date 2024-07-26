from fastapi import FastAPI, HTTPException
from async_scrap import get_results



app = FastAPI()


@app.get('/')
def root():
    return {'hell' : 'word'}


@app.get('/getSimilarity')
async def film(username1: str, username2: str):
    results =  await get_results(username1, username2)
    if not results:
        raise HTTPException(status_code=422, detail={'usernames are not valid'})
    return results
    
