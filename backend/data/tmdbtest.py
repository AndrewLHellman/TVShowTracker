import requests

def create(titleID):

    headers = {
        "accept": "application/json",
        "Authorization": "YOUR_API_KEY"
    }

    detailsURL = "https://api.themoviedb.org/3/tv/"+str(titleID)+"?language=en-US"


    titleResponse = requests.get(detailsURL, headers=headers).json()
    print(type(titleResponse))
    title = titleResponse["name"]

    # get image poster
    imageURL = "https://api.themoviedb.org/3/tv/" + str(titleID) + "/images"

    imageResponse = requests.get(imageURL, headers=headers).json()
    poster = imageResponse['posters'][0]

    # get summary
    summaryResponse = requests.get(detailsURL, headers=headers).json()
    summary = summaryResponse["overview"]

    # get genre
    genreResponse = requests.get(detailsURL, headers=headers).json()
    genre = genreResponse["genres"][0]['name']



    temp = {'title': title, 'poster': poster, 'summary': summary,'genre': genre}
    return temp


if __name__ == "__main__":
    test = create(68106)
    print(test)
    print(f"https://image.tmdb.org/t/p/w500{test['poster']['file_path']}")


