import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .database import engine, Base, SessionLocal
from .routers import products, cart, shopping_list, recommendations, smart
from seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan context:
    - Creates database tables on startup.
    - Automatically populates the database if empty so Render deployments are immediately ready.
    """
    # 1. Ensure database tables exist
    Base.metadata.create_all(bind=engine)

    # 2. Auto-seed if database is currently empty
    db = SessionLocal()
    try:
        seed_database(db, force=False)
    except Exception as e:
        print(f"[Startup Warning] Could not auto-seed database: {e}")
    finally:
        db.close()

    yield


# Initialize FastAPI App
app = FastAPI(
    title="SmartCart — Grocery Shopping Assistant API",
    description="Production-ready REST API for grocery browsing, shopping cart, smart lists, and AI recommendations.",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# -----------------------------------------------------------------------------
# CORS Middleware Configuration
# -----------------------------------------------------------------------------
# Read FRONTEND_URL from environment or fallback to allow all for static frontends
frontend_url_env = os.getenv("FRONTEND_URL", "*")

if frontend_url_env and frontend_url_env != "*":
    origins = [url.strip() for url in frontend_url_env.split(",") if url.strip()]
    # Always include common local ports for development preview
    origins.extend([
        "http://localhost:3000",
        "http://localhost:5500",
        "http://localhost:8000",
        "http://localhost:8080",
        "http://127.0.0.1:5500",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:3000",
    ])
    origins = list(set(origins))
else:
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True if origins != ["*"] else False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------------------------------
# Health Check Endpoint
# -----------------------------------------------------------------------------
@app.get("/health", summary="Service Health Check", tags=["System"])
def health_check():
    """Health check endpoint used by Render and uptime monitors."""
    return {
        "status": "ok",
        "service": "SmartCart API",
        "version": "1.0.0"
    }


@app.get("/", summary="API Root", tags=["System"])
def root():
    """API welcome endpoint providing quick links to interactive documentation."""
    return {
        "message": "Welcome to SmartCart Grocery Shopping Assistant API",
        "documentation": "/docs",
        "redoc": "/redoc",
        "health": "/health",
        "endpoints": {
            "products": "/api/products",
            "cart": "/api/cart",
            "shopping_list": "/api/shopping-list",
            "recommendations": "/api/recommendations"
        }
    }


# -----------------------------------------------------------------------------
# Register Routers
# -----------------------------------------------------------------------------
app.include_router(products.router, prefix="/api")
app.include_router(cart.router, prefix="/api")
app.include_router(shopping_list.router, prefix="/api")
app.include_router(recommendations.router, prefix="/api")
app.include_router(smart.router, prefix="/api")


# -----------------------------------------------------------------------------
# Global Exception Handlers
# -----------------------------------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Clean JSON error response to avoid leaking internal stack traces."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred while processing your request.",
            "path": str(request.url.path)
        }
    )
