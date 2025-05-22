from fastapi import APIRouter
from pathlib import Path
import json

router = APIRouter()

@router.get("/hello", tags=["Hello"])
def say_hello():
    return {"message": "Hello, world!"}

@router.get("/json", tags=["Data"])
def get_json_data():
    json_path = Path(__file__).parent.parent / "data" / "user-profiles.json"
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": "JSON file not found."}
    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON file."}
