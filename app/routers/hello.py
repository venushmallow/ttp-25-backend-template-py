from fastapi import (APIRouter, Body)
from pathlib import Path
from pydantic import BaseModel
import json

router = APIRouter()

@router.get("/hello", tags=["Hello"])
def say_hello():
    return {"message": "Hello, world!"}

@router.get("/userprofiles", tags=["User Profile"])
def get_userprofile():
    json_path = Path(__file__).parent.parent / "data" / "user-profiles.json"
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": "JSON file not found."}
    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON file."}

class userRequest(BaseModel):
    id: int
    email: str
    password: str

@router.post("/userprofiles", tags=["User Profile"])
def add_new_userprofile(
    new_user: userRequest = Body(...)
):
    json_path = Path(__file__).parent.parent / "data" / "user-profiles.json"
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(data)
        
        data.append(new_user.model_dump())

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        return data
    except FileNotFoundError:
        return {"error": "JSON file not found."}
    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON file."}