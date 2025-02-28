import os
from dotenv import load_dotenv

def load_config():
    env_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
    load_dotenv(dotenv_path=env_path)

    client_id = os.getenv("CLIENT_ID")
    print(f"Loaded CLIENT_ID: {client_id}")
    return client_id