# This script is intended to he used with the "Rizzing Up Invasive Species"
# Visual Novel to update the data of invasive species found in Massachussetts.
# To run the script, run this file with python in the directory it is found.

# DO NOT MOVE THE SCRIPT FROM THE DIRECTORY OR MOVE THE GAME

import requests
from bs4 import BeautifulSoup
import re
import json

# locate_table
# Purpose: recursively find the last child table within nested tables
# Inputs: 
#   table: table tag object
#   query: text to find in table text
# Returns: returns the last nested table with the text
def locate_table(table, query):
    sub_tables = table.find_all("table")
    if len(sub_tables) == 0:
        return table
    for new_table in sub_tables:
        if query in new_table.text:
            table = locate_table(new_table, query)
    return table

# get_hosts
# Purpose: Get the hosts of invasive species
# Inputs: 
#   soup: a beautiful soup object of the page
# Returns: A list of hosts
def get_hosts(soup):
    paragraphs = soup.find_all("p", class_="normal_copy")
    for p in paragraphs:
        if "Host" in p.text or "host" in p.text:
            hosts = []
            rows = p.find_all("li")
            if len(rows) > 0:
                for row in rows:
                    host = re.sub("\s\s+" , " ", str(row.text).replace("\n", ""))
                    host = re.sub('\(Fig.*?\)', '', host)
                    hosts.append(host)
            else:
                hosts.append(re.sub('\(Fig.*?\)', '', re.sub("\s\s+" , " ", str(p.text)).replace("\n", "")))
            # print(hosts)
            return hosts
    print("host not found")
    return None


# get_appearance
# Purpose: Get the appearane of invasive species
# Inputs: 
#   soup: a beautiful soup object of the page
# Returns: A list of appearances
def get_appearance(soup):
    tables = soup.find_all("table", border="0", cellspacing="0", cellpadding="0")
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
                appearance = re.sub("\s\s+" , " ", str(row.text)).replace("\n", "")
                appearance = re.sub('\(Fig.*?\)', '', appearance)
                appearances.append(appearance)
            print(appearances)
            return appearances
    return None


# get_damage
# Purpose: Get the damage of invasive species
# Inputs: 
#   soup: a beautiful soup object of the page
# Returns: A list of damage
def get_damage(soup):
    tables = soup.find_all("table", border="0", cellspacing="0", cellpadding="0")
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
                appearance = re.sub("\s\s+" , " ", str(row.text)).replace("\n", "")
                appearance = re.sub('\(Fig.*?\)', '', appearance)
                appearances.append(appearance)
            print(appearances)
            return appearances
    return None


# get_picture
# Purpose: Gets a picture of an invasive species
# Inputs: 
#   soup: a beautiful soup object of the page
# Notes: downloads a picture and saves it in memory
# Returns: an identifier of the picture
def get_picture(spec_soup):
    imgs = spec_soup.find_all("img")
    for img in imgs:
        if "maroon" not in img["src"] and "spacer" not in img["src"] and "thumbnails" in img["src"]:
            save_img = requests.get("https://massnrc.org/pests/pestFAQsheets/" + img["src"])
            with open(img["src"].replace("thumbnails/", "./game/animal_data_picture/"),'wb') as f:
                f.write(save_img.content)
            return img["src"].replace("thumbnails/", "")


# get_org
# Purpose: Gets all the data from an organism
# Inputs: 
#   url: the url to the organism
# Notes: saves a picture of the organism to memory
# Returns: A json/dict containing all information of the organism
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

# save_species
# Purpose: Gets all data of invasive species found in Mass.
# Notes: Saves pictures of all the data and saves jsons of all the species
def save_species():
    mainurl = "https://massnrc.org/pests/factsheets.htm"
    page = requests.get(mainurl)
    soup = BeautifulSoup(page.content, "html.parser")
    lists = soup.find_all("ul", class_="indexlist")
    invasive_list = lists[1]
    links = invasive_list.find_all('a')

    for link in links:
        try:
            org = get_org("https://massnrc.org/pests/" + link.get('href'))
            with open("./game/animal_data/"+org["name"]+".json", "w") as outfile: 
                json.dump(org, outfile)
        except Exception as error:
            print("Error occurred scraping species: ", error)
    
save_species()