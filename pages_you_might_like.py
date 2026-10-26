import json
#funtion to load json data from a file
def load_data(filename):
    with open(filename,"r") as file:
        return json.load(file)
#function to find pages a user might like based on common interests
def pages_you_might_like(user_id,data):

    #dictionary to store user interaction with pages
    user_pages = {}
    for user in data['users']:
        user_pages[user["id"]] = set(user["liked_pages"])

        #if the user not found ,return empty list
        if user_id not in user_pages:

            return []
        
        user_liked_pages = user_pages[user_id]
        page_suggestion = {}

        for other_user,pages in user_pages.items():
            if other_user!= user_id:
                shared_pages = user_liked_pages.intersection(pages)

                for page in pages:
                    if page not in user_liked_pages:
                        page_suggestion[page] = page_suggestion.get(page,0)+len(shared_pages)

        
        #sort recommended pages based on the number of shared interactions
        sorted_pages = sorted(page_suggestion.items(),key= lambda x:x[1],reverse=True)
        #here reverse=true means it give the values in descending order
        return[page_id for page_id, _ in sorted_pages]


#load data
data = load_data("massive_json_data.json")
user_id = 1
pages_recommendations = pages_you_might_like(user_id,data)
print(f"Pages you might like for user {user_id} : {pages_recommendations}")