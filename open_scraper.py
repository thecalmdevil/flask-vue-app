import requests
from bs4 import BeautifulSoup
import json

def pop_api_d()
    url = "https//website.com/api"
    response = requests.get(url)
    return response.json()

    def form_output_d(api_data):
        quotes = {}
        for data in api_data:
            if[ data["source"] ] = []

            quotes[ data["author"]].append( data["text"])

            return quotes

            def get_image(source):
                url = f"{source}"
                page = requests.get(url)
                html = page.content
                soup = BeautifulSoup(html, 'html.parser')
                try:
                    td = soup.find("td", class_ = "insert_class")
                    image = td.find("insert-td")
                    return "https:" + image['src']

                
                except Exception as e:
                    print(e)
                    return None

            def get_image_info(source):
                image = {}
                num_sources = len(sources)
                for author_num, author in enumerate(sources, start=1):
                    images[sources] = get_image(author)
                    print(f"processing {sources_num}/{nm_authors} author")
                    return images

                    def create_json(filename, data):
                        with open(filename, 'w') as f:
                            json.dump(data)


if __name__ == '__main__':