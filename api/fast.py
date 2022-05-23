from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#do I need this?
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/')
def index():
    return({'greeting':'welcome to armstracker api'})

# get exports for country
@app.get('/exports')
def exports(**kwargs):
    if 'iso_a2' in kwargs:
        return {f"{kwargs['iso_a2']}" : 'test'}
    
# get flag image for country
@app.get('/flags')
def flags(**kwargs):
    if 'iso_a2' in kwargs:
        return {f"{kwargs['iso_a2']}" : 'path_to_flag_image'}
    
# get flag emojis for sidebar
@app.get('flag_emojis')
def flag_emojis(**kwargs):
    if 'iso_a2' in kwargs:
        return {f"{kwargs['iso_a2']}" : 'path_to_flag_emoji'}