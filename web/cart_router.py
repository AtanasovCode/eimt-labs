from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database.database import get_db
from service import cart_service as carts



router = APIRouter(prefix="/api/cart", tags=["Cart"])

@router.post("/{cart_id}/buy_items")
async def buy_items(cart_id: int, db: Session = Depends(get_db)):
    try:
        carts.buy_items(db, cart__id)
        return JSONResponse(
            status_code=200,
            content={"message": f"Items from cart {cart_id} bought successfully"}
        )

    except ValueError as e:
        return JSONResponse(status_code=400, content={"message": str(e)})

