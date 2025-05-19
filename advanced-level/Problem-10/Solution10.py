from dotenv import load_dotenv
import os

def load_env(env_file=".env"):
    load_dotenv(env_file)
    return {key: os.environ[key] for key in os.environ if key in open(env_file).read()}

# Test the function (assume .env with API_KEY=abc123)
print(load_env())