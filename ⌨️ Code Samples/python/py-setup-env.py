# WITHIN CODE 
import os
os.environ['MY_VARIABLE'] = 'my_value'
value = os.environ.get('MY_VARIABLE')
db_password = os.environ.get('DB_PASSWORD') # value set in shell
print(value)

# FROM ENV FILE 
# load .env file 
#pip install python-dotenv
DB_HOST=localhost
DB_USER=admin

from dotenv import load_dotenv
import os
load_dotenv()  # loads from .env into os.environ
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')