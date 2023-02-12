import requests #download data from net so use requests to read html 
import re # for parsing and extracting link in html code

class Webcrawler:
    
    def __init__(self):
        #we want to avoid revisiting the same website over and over again
        self.discovered_websites = []
        
        #bfs implementation
        
    def crawl(self, start_url):
        
        queue = [start_url]
        self.discovered_websites.append(start_url)
        
        while queue:
            actual_url = queue.pop(0)
            print(actual_url)
            
            #this is the raw html representation of the given website(URL)
            actual_url_html = self.read_raw_html(actual_url)
            
            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)
    
    def get_links_from_html(self, raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-dA-F]{2}))", raw_html)

    def read_raw_html(self, url):
        raw_html = ''
        
        try:
            raw_html = requests.get(url).text
        #some sites dont permit the access to their raw html code
        except Exception as e:
            pass
        
        return raw_html

if __name__=='__main__':
    # a sample case has been give below
    """
    crawler = Webcrawler()
    crawler.crawl("https://www.cnn.com")
    """
    pass
