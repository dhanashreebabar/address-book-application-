from sqlalchemy.orm import Session
from app.models import Address
import math

def create_address(db: Session, address: Address) -> Address:
    db.add(address)
    db.commit()
    db.refresh(address)
    return address

def get_address(db: Session, address_id: int) -> Address | None:
    return db.query(Address).filter(Address.id == address_id).first()

def delete_address(db: Session, address_id: int) -> bool:
    address = db.query(Address).filter(Address.id == address_id).first()
    if address:
        db.delete(address)
        db.commit()
        return True
    return False

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0  # Earth radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    return R * c