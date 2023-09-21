from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re
from datetime import datetime

app = FastAPI()


# Model knjige
class Book(BaseModel):
    id: int
    naslov: str
    autor: str
    isnb: str
    datum: str


# Validator koristeci regex koji mora biti tacno 13 cifara
def validate_isbn(isbn: str):
    if not re.match(r'^[0-9]{13}$', isbn):
        raise ValueError("ISBN mora sadrzati tacno 13 cifara.")
    return isbn


# Validator datuma
def validate_date(date: str):
    try:
        parsed_date = datetime.strptime(date, '%d.%m.%Y.')
    except ValueError:
        raise ValueError("Datum mora biti u formatu dd.mm.yyyy.")
    return date


# Lokalno cuvanje
db = []


# Dodavanje knjige
@app.post("/books", response_model=Book)
def add_book(book: Book):
    for sameID in db:
        if sameID.id == book.id:
            raise HTTPException(status_code=400, detail=f"Knjiga sa ID {book.id} vec postoji.")

    try:
        book.isnb = validate_isbn(book.isnb)
        book.datum = validate_date(book.datum)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Generisanje ID-a
    book.id = len(db) + 1
    db.append(book)
    return book


# Pretraga svih knjiga
@app.get("/books", response_model=list[Book])
def get_books():
    return db


# Petraga knjige po ID-u
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Knjiga sa ID {book_id} nije pronadjena!")


# Izmena knjige
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: Book):
    for i, book in enumerate(db):
        if book.id == book_id:
            try:
                book_update.isnb = validate_isbn(book_update.isnb)
                book_update.datum = validate_date(book_update.datum)
                db[i] = book_update
                return book_update
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
    raise HTTPException(status_code=404, detail=f"Knjiga sa ID {book_id} nije pronadjena!")


# Brisanje knjige po ID-u
@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id:int):
    for i, book in enumerate(db):
        if book.id == book_id:
            delete_book = db.pop(i)
            return delete_book
    raise HTTPException(status_code=404, detail=f"Knjiga sa ID {book_id} nije pronadjena!")
