from fastapi import APIRouter, Depends
from services.ai_service import AIService

router = APIRouter()

# Inject the service via DI
def get_ai_service():
    return AIService()

@router.post("/analyze")
async def analyze_endpoint(repo_url: str, service: AIService = Depends(get_ai_service)):
    # The router does NO logic. It delegates instantly to the Service Layer.
    result = await service.analyze_codebase(repo_url)
    return result