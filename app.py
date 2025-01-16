from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId
import os

# MongoDB connection setup
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["user_management"]
user_collection = db["users"]

app = FastAPI()

# User model
class User(BaseModel):
    name: str
    email: str
    age: int

# Helper to serialize MongoDB documents
def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"],
    }

# API 1: Create user
@app.post("/users/", response_model=dict)
def create_user(user: User):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    result = user_collection.insert_one(user.dict())
    created_user = user_collection.find_one({"_id": result.inserted_id})
    return serialize_user(created_user)

# API 2: View/get user
@app.get("/users/{user_id}", response_model=dict)
def get_user(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    return serialize_user(user)

# API 3: List users and edit user details
@app.get("/users/", response_model=List[dict])
def list_users():
    users = user_collection.find()
    return [serialize_user(user) for user in users]

@app.put("/users/{user_id}", response_model=dict)
def edit_user(user_id: str, user: User):
    update_result = user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict()}
    )

    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")

    updated_user = user_collection.find_one({"_id": ObjectId(user_id)})
    return serialize_user(updated_user)

# Optional: Delete user
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: str):
    delete_result = user_collection.delete_one({"_id": ObjectId(user_id)})

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")

    return {"message": "User deleted successfully."}
