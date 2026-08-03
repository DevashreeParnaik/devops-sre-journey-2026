from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ShopSphere API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")


@api_router.get("/health")
def health():
    return {
        "status": "UP"
    }


@api_router.get("/products")
def products():
    return [
        {
            "id": 1,
            "name": "Laptop"
        },
        {
            "id": 2,
            "name": "Phone"
        }
    ]


app.include_router(api_router)