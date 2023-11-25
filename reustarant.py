class restaurant_layout: # Restaurant Class
    name=""
    description=""
    keywords=[]

def display_restaurant(restaurant: restaurant_layout):
    print(f'---------------------------\n\n')
    print(f'Name: {restaurant.name}\n')
    print(f'Description: {restaurant.description}\n')
    print(f'Types: {restaurant.keywords}')
    print(f'---------------------------\n\n')

def display_searched_restaurants_list(argument_list,restaurants_list): # Displays the List of searched Restaurants
    for restaurant in restaurants_list:
        counter=0
        for keyword in argument_list:
            if keyword in restaurant.keywords:
                counter=counter+1;
            if counter == len(argument_list):
                display_restaurant(restaurant)
                break
def create_list_restaurant(restaurants_collection): # Parses the information from Database and creates the list of restaurants
    if restaurants_collection:
        new_list = []
        for doc in restaurants_collection:
            item=restaurant_layout()
            item.keywords=doc['keywords']
            item.name=doc['name']
            item.description=doc['description']
            new_list.append(item)
    else:
        return 0
    return new_list
