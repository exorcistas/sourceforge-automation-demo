from sourceforge import SFScraper

sf = SFScraper()
urls = sf.get_popular_project_urls(1)
print(urls)