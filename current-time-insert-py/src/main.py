import datetime
import pytz

from dotenv import load_dotenv
from database import insert_data
from os import environ

# Load environment variables from .env
load_dotenv()                          

# Main program
def main():

    # Get current time (Uruguay)
    current_time = datetime.datetime.now(pytz.timezone('America/Montevideo')).strftime("%d/%m/%Y, %H:%M:%S")

    # Create JSON
    json_object = {
        'current_time' : current_time
    }

    # Insert JSON
    result = insert_data(None, json_object)
    
    if (result):
        print('Successfully inserted new registry into database.\nRegistry ', json_object)
    else:
        print('Something went wrong :(')

# Run Main program
if __name__ == '__main__':
    main()