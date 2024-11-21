from dotenv import load_dotenv
import os

load_dotenv()

AZURE_DB_PW_DEV = os.getenv("AZURE_DB_PW_DEV")
AZURE_DB_UID = os.getenv("AZURE_DB_UID")
