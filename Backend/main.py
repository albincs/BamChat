from fastapi import FastAPI
app = FastAPI(title="3D Design Generator")

@app.get("/")
def root():
    return {"message": "Backend connected successfully!"}
