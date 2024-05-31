from dotenv import load_dotenv
import os

load_dotenv()

conf = {
    "HOST": os.getenv("HOST"),
    "PORT": os.environ.get("PORT", 5000),
    "MONGODB_CONNECTION": os.getenv("MONGODB_CONNECTION"),
    "MONGODB_NAME": os.getenv("MONGODB_NAME"),
    "MONGODB_CONNECTION_LOCAL": os.getenv("MONGODB_CONNECTION_LOCAL"),
    "MONGODB_NAME_LOCAL": os.getenv("MONGODB_NAME_LOCAL"),
}