from langchain_openai import ChatOpenAI
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

async def generate_llm_response(prompt: str) -> str:
    try:
        llm = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )
        response = await llm.apredict(prompt)
        return response
    except Exception as e:
        logger.error(f"LLM generation failed: {str(e)}")
        return "Unable to generate response"