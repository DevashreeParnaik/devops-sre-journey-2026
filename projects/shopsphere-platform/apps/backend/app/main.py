from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ShopSphere API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    #allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/products")
def products():
    return [
        {
            "id":1,
            "name":"Laptop"
        },
        {
            "id":2,
            "name":"Phone"
        }
    ]