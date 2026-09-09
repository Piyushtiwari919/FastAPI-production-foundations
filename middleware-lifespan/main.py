from fastapi import FastAPI, Request, Depends
from lifespan import lifespan, FakeMLModel
from middlewares import benchmark

app = FastAPI(lifespan=lifespan)

app.middleware("http")(benchmark)


def get_ml_model(request: Request) -> FakeMLModel:
    return request.app.state.ml_models["my_model"]


@app.get("/predict")
async def predict_res(text: str, model: FakeMLModel = Depends(get_ml_model)):
    return model.predict(text)
