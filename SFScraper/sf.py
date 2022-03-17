import requests as req
from bs4 import BeautifulSoup
import json


class SFScraper():
    def __init__(self):
        self.base_url = "https://sourceforge.net"
        print("SFScraper initialized")

    """
    Method scrapes SF website for popular projects, one page at a time
    """
    def getPopularProjectsByPage(self, pagenum):
        urls = []
        resp = req.get(self.base_url + "/directory/?sort=popular&page=" + str(pagenum))
        if (resp.status_code == 200):
            soup = BeautifulSoup(resp.content, "html.parser")
            project_tags = soup.find_all("a", attrs={"class": "result-heading-title"})
            urls += [self.base_url + x["href"] for x in project_tags]
        else:
            raise(f"Return status not OK: {resp.status_code}")
        return urls

    """
    Method uses SF API to fetch project release info
    Note: SF originally named latest releases as 'best releases'
    """
    def getProjectBestReleases(self, url):
        resp = req.get(url + "best_release.json")
        if (resp.status_code == 200):
            releases = json.loads(resp.content)
        else:
            raise(f"Return status not OK: {resp.status_code}")
        return releases


if __name__ == "__main__":
    print("DEMO")
    sf = SFScraper()
    urls = []
    for pagenum in range(1, 5):
        urls += sf.getPopularProjectsByPage(pagenum)

    print(f"Got top {len(urls)} projects")
    print("Filtering Windows PE32 executables...")
    for url in urls:
        rel = sf.getProjectBestReleases(url)
        try:
            if (rel['platform_releases']['windows']['file_type'] == "PE32 executable"):
                print(url[:len(url)-1] + rel['platform_releases']['windows']['filename'])
        except:
                print("[EXCEPTION] Releases not found in: " + url)