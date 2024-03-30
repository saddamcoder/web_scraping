import httpx
import time
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup

def get_data(store: str, url: str, selector: str):
    """
       get data from url and return html string
       Args:
           store (string): The client's request to the server.
       Returns:
           HttpResponseRedirect: Redirects the user to the Login page.
       """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.currys.co.uk/"
    }
    # Use a session object to handle cookies
    with httpx.Client() as client:
        # Send the request
        response = client.get(url, headers=headers)

        # Delay to mimic human behavior
        time.sleep(3)

        # Ensure that cookies are set in subsequent requests
        client.cookies.extract_cookies(response)
        client.headers.update(headers)

        # Debugging: Print out cookies before and after extraction
        # print("Cookies before extraction:", client.cookies.jar)
        # client.cookies.extract_cookies(response)
        # print("Cookies after extraction:", client.cookies.jar)

    # Check if the request was successful
    if response.status_code == 200:
        html = BeautifulSoup(response.text, 'html.parser')
        print(html)
        element = html.select_one(selector)
        price = ""
        if element is not None:
            price = element.text.strip()
        return {"store": store, "price": price}
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None



    # html = HTMLParser(response.text)
    # element = html.css_first(selector)
    # price = ""
    # if element is not None:
    #     price = element.text().strip()
    # return {"store": store, "price": price}

def main():
    results = [get_data(
        "Amozon",
        "https://www.currys.co.uk/products/acer-swift-go-14-laptop-intel-core-i7-512-gb-ssd-silver-10250732.html",
        "span.value"
        ),
    ]
    print(results)


if __name__ == "__main__":
    main()