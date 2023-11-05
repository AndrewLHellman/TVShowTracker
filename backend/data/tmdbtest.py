import requests

# tvdb key 0c1b4bb1-5624-45c4-9240-cba3f7c373ec



def create(titleID):

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYzM5NWRiMDY5Zjc0NDU0OTQ5Mjg1MTYxYzdjY2ZlMyIsInN1YiI6IjY1NDY4NTFkZDU1YzNkMDBjNWJlNTFjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iAxli90QWWVj0x3mRsRd-Rtt4F14RRInx396fIoE8PA"
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


