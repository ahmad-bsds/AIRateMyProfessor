import json
from dotenv import load_dotenv
import os

# Json read utility.
def read_json_file(file_path):
  """Reads a JSON file and returns its contents as a Python object.

  Args:
    file_path: The path to the JSON file.

  Returns:
    The contents of the JSON file as a Python object (typically a dictionary or list).
  """

  with open(file_path, 'r') as f:
    data = json.load(f)
  return data

# Environment variable load utility.
def load_env(name: str):
  """function to load environment variable."""
  # Specify the path to your .env file
  env_path = '../etc/secrets/.env_var' # ../.env

  # Load the .env file
  try:
   load_dotenv(dotenv_path=env_path)
   print("Env variables loaded successfully!")
  except:
    print("Env variables loading failed!")

  # Now you can access the environment variables
  return os.getenv(name)
