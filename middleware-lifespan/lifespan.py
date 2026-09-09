from contextlib import asynccontextmanager
from fastapi import FastAPI


class FakeMLModel:
    def predict(self, text):
        return f"Prediction for: {text}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ml_models = {"my_model": FakeMLModel()}

    yield

    app.state.ml_models.clear()
