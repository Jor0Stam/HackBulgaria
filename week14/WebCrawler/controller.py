from bs4 import BeautifulSoup
from requests import get, session

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from servers import a
import matplotlib.pyplot as plt


Base = declarative_base()
engine = create_engine('sqlite:///CrawledServers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_server(url):
    result = get(url).headers['Server'].split("/")
    return result[0]


def generate_clickables(url):
    soup = BeautifulSoup(get(url).text, 'html.parser')
    for link in soup.find_all('a'):
        yield(link.get('href'))


def format_link(link, url):
    if "link.php?id=" not in link:
        pass
    elif link[:link.index("ink.php?id=")] == "l":
        return url + link
    return link


def crawl_it(url):
    craw_session = session()
    craw_session.keep_alive = False
    servers = {}
    for link in generate_clickables(url):
        try:
            if not link or link == '#top':
                continue
            link = format_link(link, url)
            curr_server_name = get_server(link)
            print(curr_server_name)
            if curr_server_name in servers:
                servers['curr_server_name'] += 1
            else:
                servers['curr_server_name'] = 1
            # if session.query(
            #         Server).filter(Server.server == curr_server_name).one():

            #     session.query(
            #         Server).update(Server).where(
            #         Server.server == curr_server_name).\
            #         values(Server.times_used=Server.times_used + 1)
            # else:
            #     session.add(Server(server=curr_server_name, times_used=1))
        except:
            print("Exception")
    print(servers)
    with open("servers.py", "w") as f:
        f.write(servers)


def display_it(result):
    plt.bar(range(len(result)), result.values(), align='center')
    plt.xticks(range(len(result)), result.keys())
    plt.show()


def main():
    mother_url = "http://register.start.bg/"
    # crawl_it(mother_url)
    srvs = {}
    for server in a.split("\n"):
        if server in srvs.keys():
            srvs[server] += 1
        else:
            srvs[server] = 1
    print(a.split("\n"))
    display_it(srvs)



if __name__ == "__main__":
    main()
