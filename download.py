import requests
import json


def main(start, end):
 for i in range(start, end):
   url = "https://api.opensea.io/api/v1/asset/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/" + str(1)
   response = json.loads(requests.request("GET", url).text)
   print(response)
   img_data = requests.get(response[ 'image_original_url']).content
   with open('./' + str(i) + '.png', 'wb') as handler:
    handler.write(img_data)


start = 1
end = 10000
main(start,end)
