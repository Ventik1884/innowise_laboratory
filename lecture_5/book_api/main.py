from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional

DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

Base.metadata.create_all(bind=engine)

from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class BookRead(BookCreate):
    id: int
    class Config:
        orm_mode = True

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /books/ - добавить книгу
@app.post("/books/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# GET /books/ - получить все книги
@app.get("/books/", response_model=List[BookRead])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Book).offset(skip).limit(limit).all()

# DELETE /books/{book_id} - удалить книгу по ID
@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted"}

# PUT /books/{book_id} - обновить книгу
@app.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = book.title
    db_book.author = book.author
    db_book.year = book.year
    db.commit()
    db.refresh(db_book)
    return db_book

# GET /books/search/ - поиск книг по title, author, year
@app.get("/books/search/", response_model=List[BookRead])
def search_books(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)
    return query.all()