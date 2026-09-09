import uuid
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import contextvars

# 1. Create a global context variable to hold the UUID for the current async task
request_id_context = contextvars.ContextVar("request_id", default="unknown")


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 2. Check if the incoming request already has an ID (if it came from another microservice)
        # If not, generate a brand new UUIDv4.
        req_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))

        # 3. Store it in the context variable so our logger can find it later
        request_id_context.set(req_id)
        # 4. Attach it to the request state just in case we need it in the route
        request.state.correlation_id = req_id

        # 5. Execute the actual route logic
        response = await call_next(request)

        return response


app = FastAPI()
app.add_middleware(CorrelationIdMiddleware)


@app.post("/auth")
async def auth_post(id: int):
    return {"id": id}
