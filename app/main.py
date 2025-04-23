from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.endpoints import items
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#------------------------------Lifespan event handler------------------------------#
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    #------------------------------Startup logic------------------------------#
    logger.info("Application startup complete")
    yield
    #------------------------------Shutdown logic------------------------------#
    logger.info("Application shutdown complete")

app = FastAPI(
    title="FastAPI Production App",
    description="FastAPI with LLM and CRUD",
    version="1.0.0",
    lifespan=app_lifespan
)

#------------------------------CORS configuration------------------------------#
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#------------------------------Include routers------------------------------#
app.include_router(items.router, prefix="/api/v1")