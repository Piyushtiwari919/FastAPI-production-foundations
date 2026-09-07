from fastapi import Depends, FastAPI

app = FastAPI()


def get_db():
    db = "Fake Database Connection"
    try:
        yield db
    finally:
        # db.close()
        print("DB IS CLOSED")


@app.get("/users/")
async def read_users(db_session=Depends(get_db)):
    # FastAPI automatically runs get_db() and injects the result here
    return {"data": db_session}
