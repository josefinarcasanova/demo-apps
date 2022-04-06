import datetime

from dotenv import load_dotenv
from database import connect_to_database, get_data, insert_data
from os import environ

# Load environment variables from .env
load_dotenv()                          

# Main program
def main():
    current_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    json_object = {
        'current_time' : current_time
    }

    result = insert_data(json_object)
    
    if (result):
        print('Successfully inserted new registry into database.\nRegistry ', json_object)

if __name__ == '__main__':
    main()                      # Run Main program