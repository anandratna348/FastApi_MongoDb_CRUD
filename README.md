# FastApi_MongoDb_CRUD
Follow these steps to run
### 1. **Install Dependencies**
Ensure you have Python installed (preferably version 3.9 or later). Install the required dependencies using `pip`:

```bash
pip install fastapi pymongo uvicorn pydantic
```

### 2. **Set Up MongoDB**
- **Local MongoDB**: Make sure MongoDB is installed and running on your local machine. The default connection URI (`mongodb://localhost:27017`) is used in the code.
  - [Install MongoDB](https://www.mongodb.com/docs/manual/installation/) if it's not already installed.
- **Cloud MongoDB**: If you prefer using MongoDB Atlas or another hosted solution, replace the `MONGO_URI` in the code with your MongoDB connection string.

### 3. **Save the Code**
Save the code in a Python file, e.g., `app.py`.

### 4. **Run the Application**
Use Uvicorn to run the FastAPI application:

```bash
uvicorn app:app --reload
```

- `app` is the filename (without the `.py` extension).
- `--reload` enables auto-reloading for development purposes.

### 5. **Access the API**
Once the server starts, you'll see output like this:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

You can now access your API at `http://127.0.0.1:8000`.

### 6. **Test the API**
#### Swagger UI:
Visit the interactive Swagger UI documentation at:
```
http://127.0.0.1:8000/docs
```

#### Example API Endpoints:
- **Create User**: `POST /users/`
- **Get User**: `GET /users/{user_id}`
- **List Users**: `GET /users/`
- **Edit User**: `PUT /users/{user_id}`
- **Delete User** (optional): `DELETE /users/{user_id}`

#### Example Request using `curl` or Postman:
- **Create User**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com", "age": 30}'
  ```

- **Get User**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/users/<user_id>"
  ```

Replace `<user_id>` with the actual ID returned by the `create_user` API.

---

Let me know if you encounter any issues or need further help!
