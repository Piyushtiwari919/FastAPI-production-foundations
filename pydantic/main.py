from fastapi import Body, FastAPI
from schema import UserProfile

app = FastAPI()


ITEM_BODY = Body(embed=True)


@app.post("/user")
async def save_user(user: UserProfile = ITEM_BODY):
    return {"address": user.address}
