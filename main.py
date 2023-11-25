
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import reustarant as res
import search_keyword as key


if __name__ == '__main__':
    uri = "mongodb+srv://Sorzys:matamata4521@cluster0.ud1qpdn.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))  # Connects to the Database of Restaurants

    database = client.City_Leisures # Assigns the Database Information to Variable "database"

    restaurants_collection=database["Restaurants"] # Assigns the Collection of Restaurants

    restaurants_collection=restaurants_collection.find() # Creates the Raw List of Restaurants
    restaurants=res.create_list_restaurant(restaurants_collection) # Creates the Python List of Restaurants from the Raw List
    keywords=key.create_list_keywords(restaurants) # Creates the List of Possible Keywords the user can search
    end=1
    while end:
        isCorrect=False
        while not isCorrect:
            argument_list=input("What kind of Restaurants are you looking for?\n") # Input User
            isCorrect=key.check_correction(argument_list) # Checks if the Input has only spaces or is NULL
        argument_list= key.form_search_keywords(argument_list) # Creates the key list of arguments
        argument_list= key.auto_complete(argument_list,keywords) # In case of the User giving only parts of the possible keyword. auto_complete() will try and complete them
        res.display_searched_restaurants_list(argument_list,restaurants) # Display the possible Restaurants that the user has searched

        end_question=input("Do you want to end your search? [Y/N]") # End Program
        if end_question=="Y" or end_question=="y":
            end=0




            




# See PyCharm help at https://www.jetbrains.com/help/pycharm/