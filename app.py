from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="Reading List API")
books=[]
class Book(BaseModel):
    title:str
    author:str="Unknown"
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/books")
def list_books(): return books
@app.post("/books",status_code=201)
def add_book(book:Book):
    item={"id":len(books)+1,**book.model_dump()}; books.append(item); return item
