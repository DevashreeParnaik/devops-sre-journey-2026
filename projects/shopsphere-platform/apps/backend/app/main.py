from fastapi import FastAPI

app = FastAPI(
    title="ShopSphere API"
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