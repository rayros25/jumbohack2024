import requests
from bs4 import BeautifulSoup
import re
import os
import json

def locate_table(table, query):
    sub_tables = table.find_all("table")
    if len(sub_tables) == 0:
        return table
    for new_table in sub_tables:
        if query in new_table.text:
            table = locate_table(new_table, query)
    return table

def get_hosts(soup):
    paragraphs = soup.find_all("p", class_="normal_copy")
    for p in paragraphs:
        if "Host" in p.text or "host" in p.text:
            hosts = []
            rows = p.find_all("li")
            if len(rows) > 0:
                for row in rows:
                    host = re.sub("\s\s+" , " ", str(row.text).replace("\n", ""))
                    hosts.append(host)
            else:
                hosts.append(re.sub("\s\s+" , " ", str(p.text)).replace("\n", ""))
            # print(hosts)
            return hosts
    print("host not found")
    return None



def get_appearance(soup):
    tables = soup.find_all("table", border="0", cellspacing="0", cellpadding="0")
    # If the page has symptoms
    found = False
    for table in tables:
        if "Symptoms" in table.text:
            query = "Symptoms"
            found = True
        elif "Key" in table.text:
            query = "Key"
            found = True
        if found:
            table = locate_table(table, query)
            appearances = []
            # Gets the rows
            rows = table.find_all("li")
            if len(rows) == 0:
                rows = table.find_all("td", class_="normal_copy")
            # Attach rows to the appearances list
            for row in rows:
                appearance = (re.sub("\s\s+" , " ", str(row.text)).replace("\n", ""))
                appearances.append(appearance)
            print(appearances)
            return appearances
    return None

def get_damage(soup):
    tables = soup.find_all("table", border="0", cellspacing="0", cellpadding="0")
    # If the page has symptoms
    found = False
    for table in tables:
        if "amage" in table.text:
            query = "amage"
            found = True
        if found:
            table = locate_table(table, query)
            appearances = []
            # Gets the rows
            rows = table.find_all("li")
            if len(rows) == 0:
                rows = table.find_all("td", class_="normal_copy")
            # Attach rows to the appearances list
            for row in rows:
                appearance = (re.sub("\s\s+" , " ", str(row.text)).replace("\n", ""))
                appearances.append(appearance)
            print(appearances)
            return appearances
    return None

def get_picture(spec_soup):
    imgs = spec_soup.find_all("img")
    for img in imgs:
        if "maroon" not in img["src"] and "spacer" not in img["src"] and "thumbnails" in img["src"]:
            save_img = requests.get("https://massnrc.org/pests/pestFAQsheets/" + img["src"])
            with open(img["src"].replace("thumbnails/", "./MassInvasiveSpecies/Pictures/"),'wb') as f:
                f.write(save_img.content)
            return img["src"].replace("thumbnails/", "")

def get_org(url):
    org_dict = {}
    
    org_dict["url"] = url
    print(url)
    spec_soup = BeautifulSoup((requests.get(url)).content, "html.parser")
    org_dict["name"] = spec_soup.find("title").text
    org_dict["description"] = spec_soup.find("meta", {"name":"description"})['content']
    print(org_dict["description"])
    org_dict["hosts"] = get_hosts(spec_soup)
    org_dict["appearance"] = get_appearance(spec_soup)
    org_dict["damage"] = get_damage(spec_soup)
    org_dict["picture"] = get_picture(spec_soup)
    return org_dict

def save_species():
    mainurl = "https://massnrc.org/pests/factsheets.htm"
    page = requests.get(mainurl)
    soup = BeautifulSoup(page.content, "html.parser")
    lists = soup.find_all("ul", class_="indexlist")
    invasive_list = lists[1]
    links = invasive_list.find_all('a')
    
    if not os.path.exists("./MassInvasiveSpecies"):
        os.mkdir("./MassInvasiveSpecies")
    if not os.path.exists("./MassInvasiveSpecies/Pictures"):
        os.mkdir("./MassInvasiveSpecies/Pictures")

    for link in links:
        try:
            org = get_org("https://massnrc.org/pests/" + link.get('href'))
            with open("./MassInvasiveSpecies/"+org["name"]+".json", "w") as outfile: 
                json.dump(org, outfile)
        except Exception as error:
            print("Error occurred scraping species: ", error)

        
save_species()