from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco de dados
DATABASE_URL = "sqlite:///./data.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    name: str

class ItemResponse(ItemCreate):
    id: int

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    db = SessionLocal()
    db_item = Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.get("/items/", response_model=list[ItemResponse])
def read_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        db.close()
        raise HTTPException(status_code=404, detail="Achei Não")
    db_item.name = item.name
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        db.close()
        raise HTTPException(status_code=404, detail="Achei Não")
    db.delete(db_item)
    db.commit()
    db.close()
    return {"message": "Item jogado no mar do esquecimento"}