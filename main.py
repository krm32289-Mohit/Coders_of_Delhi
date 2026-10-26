import json
#load data
with open("json_dump.json","r") as file:
    data = json.load(file)
    print(data)
    print(type(data))
#Display users and their connection

def display_user(data):
    print("Users and their connection")
    for user in data['users']:
        print(f"{user['id']}.{user['name']} is friends with {user['friends']} and liked_pages are {user['liked_pages']}")

    print("\nPages Information")
    for page in data['pages']:
        print(f"{page['id']} : {page['name']}")
    
display_user(data)



import json
with open("json_dump.2.json","r") as f:
    data2 = json.load(f)
    print(data2)

def clean_data(data2):
    #remove users with missing values
    data2['users'] = [user for user in data2['users'] if user ["name"].strip()]
    #remove duplicate values
    for user in data2['users']:
        user["friends"] = list(set(user['friends']))

    #remove inactive users
    data2['users'] = [user for user in data2['users'] if user["friends"] or user["liked_pages"]]

#Remove duplicate pages
    unique_pages = {}
    for page in data2['pages']:
        unique_pages[page['id']] = page
    data2['pages'] = list(unique_pages.values())
    return data2

# load the data
with open("json_dump.2.json","r") as file:
    data2 = json.load(file)
    # print(data)
    data2 = clean_data(data2)

    #save the clean data in file
    with open("cleaned_data_2","w") as file:
        json.dump(data2,file,indent=4)
print("Data clean successfully")