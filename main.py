from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Разрешаем запросы от Mini App
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Простое хранилище (потом заменим на БД)
users = {}

class TapData(BaseModel):
    user_id: int
    taps: int

@app.get("/")
def root():
    return {"status": "NEON VOID server online"}

@app.post("/tap")
def save_tap(data: TapData):
    users[data.user_id] = data.taps
    return {
        "ok": True,
        "user_id": data.user_id,
        "taps": users[data.user_id]
    }

@app.get("/get/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "taps": users.get(user_id, 0)
    }
