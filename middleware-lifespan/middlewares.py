from fastapi import Request
import time

async def benchmark(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    response.headers["X-Process-Time"] = str(end_time - start_time)
    return response

