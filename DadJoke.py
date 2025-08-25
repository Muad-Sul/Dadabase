import requests #brings in the request library, lets me make HTTP requests to website

base_url = "https://icanhazdadjoke.com"
#stores main website into a variable

def get_dadJoke():
# asks website for a joke in JSON format
    url = "https://icanhazdadjoke.com"
    #sending request to this site
    headers = {"Accept": "application/json"}
    #This tells website that I want the joke in JSON format
    response = requests.get(url, headers=headers)
    #sends GET request to website.

    if response.status_code == 200:
    #checks if the request worked. 200 is the code for successful request
        dadJoke_data = response.json()
        #turns response and makes it a dictionary so its accessed easily
        return dadJoke_data['joke']
        # Return the actual joke string to whoever called the function
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return "Failed to load joke!"
    # if response unsuccessful, it prints error code and message


if __name__ == "__main__":
#checks if runnig file directly
    joke = get_dadJoke()
    #calls function to get dad joke and saves it into variable
    print(joke)
