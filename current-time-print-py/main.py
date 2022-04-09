import datetime
import pytz

from dotenv import load_dotenv
from os import environ

# Load environment variables from .env
load_dotenv()                          

# Main program
def main():
    current_time = datetime.datetime.now(pytz.timezone('America/Montevideo')).strftime("%d/%m/%Y, %H:%M:%S")
    print("The current date and time in Uruguay are:", current_time)

if __name__ == '__main__':
    main()                      # Run Main program