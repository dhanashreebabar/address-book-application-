from fastapi import FastAPI,Depends, HTTPException
from app.database import AsyncSessionLocal, engine, Base
from sqlalchemy.orm import Session
from app import models, schemas, app as address_app
from app.models import Address
from app.app import create_address, get_address, delete_address, haversine


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Address Management API")

def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addresses/", response_model=schemas.AddressRead)
async def create_new_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    db_address = models.Address(**address.dict())
    return create_address(db, db_address)

@app.get("/addresses/", response_model=list[schemas.AddressRead])
async def read_addresses(db: Session = Depends(get_db)):
    addresses = db.query(Address).all()
    return addresses
    
@app.get("/addresses/{address_id}", response_model=schemas.AddressRead)
async def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = get_address(db, address_id)
    if db_address is None:
        raise HttpException(status_code=404, detail="Address not found")
    return db_address

@app.delete("/addresses/{address_id}", response_model=dict)
async def delete_existing_address(address_id: int, db: Session = Depends(get_db)):
    success = delete_address(db, address_id)
    if not success:
        raise HttpException(status_code=404, detail="Address not found")
    return {"detail": "Address deleted successfully"}

@app.get("/addresses/distance/", response_model=dict)
async def calculate_distance(  
    lat1: float, lon1: float, lat2: float, lon2: float
):
    distance = haversine(lat1, lon1, lat2, lon2)
    return {"distance_km": distance}        