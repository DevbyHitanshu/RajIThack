from ./main_kg copy.ipynb import KG
from numpy import np
from fastapi import FastAPI
import uvicorn
# from "file" import file
from typing import List, Optional
from pydantic import BaseModel
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
# import spacy
# from spacytextblob.spacytextblob import SpacyTextBlob
# nlp = spacy.load('en_core_web_sm')
# nlp.add_pipe('spacytextblob')
# app = Flask(__name__)
# api = Api(app)
# Declaring our FastAPI instance
app = FastAPI()
 
# Defining path operation for root endpoint
@app.route("/")
def get_index():
    return app.send_static_file("index.html")

@app.route("/search")
def get_search():
    def KG():





 
# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name : str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f', {name}'}

class request_body(BaseModel):

    



def NLP(s:str):
    def KG(s:str):
        return np.arr[i][j]
    
    arr = response(arr)
    return arr
app = Flask(__name__)
api = Api(app)

# @route.post("/url")
# def route(request_body):
#     array = 
#     return np.array


if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.info("Starting on port %d, database is at %s", port, url)
    app.run(port=port)



# def xyz():
#     def abc():
#         return [][]
#     pydantics schema(class h ye)

