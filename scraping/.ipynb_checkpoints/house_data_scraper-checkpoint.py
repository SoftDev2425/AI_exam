import csv
import time
import argparse
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from accept_terms import accept_terms
from coordinates import get_coordinates

browser = webdriver.Firefox()
browser.get('https://www.dingeo.dk')
time.sleep(2)

accept_terms(browser)

def save_to_csv(data, filename):
    fieldnames = ['Address', 'X', 'Y', 'Price', 'Type', 'Size', 'Squaremeter price', 'Energy class', 'Url']
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def load_visited_urls(filename):
    visited_urls = []
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Address', 'X', 'Y', 'Price', 'Type', 'Size', 'Squaremeter price', 'Energy class', 'Url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        return visited_urls

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                visited_urls.append(row['Url'])
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        
    return visited_urls

def scrape_address(browser):
    try:
        address = browser.find_element(By.XPATH, '/html/body/div/div[6]/div[1]/div[2]/div[1]/h1').text
        match = re.match(r'^(.*?), \d{4} .+', address)
        if match:
            return match.group(1)
        return address
    except:
        print("No address found")
        return None

def scrape_price(browser):
    try:
        price = browser.find_element(By.XPATH, '/html/body/div/div[6]/div[1]/div[2]/div[1]/div[1]/div/div[2]/dl/dd[1]').text
        return price
    except:
        print("No price found")
        return None
    
def scrape_type(browser):
    try:
        type = browser.find_element(By.XPATH, '//*[@id="ctrldiv"]/div[6]/div[1]/div[2]/div[1]/div[1]/div/div[2]/dl/dd[2]').text
        return type
    except:
        print("No type found")
        return None

def scrape_squaremetres(browser):
    try:
        squaremetres = browser.find_element(By.XPATH, '/html/body/div/div[6]/div[1]/div[2]/div[1]/div[1]/div/div[2]/dl/dd[4]').text
        return squaremetres
    except:
        print("No square metres found")
        return None

def scrape_energy_class(browser):
    try:
        # Try to extract energy class from text
        try:
            energy_class = browser.find_element(By.XPATH, '/html/body/div/div[6]/div[1]/div[2]/div[28]/div/div[2]/div/div[1]/p[1]').text
            regex_pattern = r"energimærke\s*(A2020|A2015|A2010|A|B|C|D|E|F|G)"
            match = re.search(regex_pattern, energy_class, re.IGNORECASE)
            if match:
                return match.group(1).upper()
        except NoSuchElementException:
            pass

        # If text extraction fails, try to extract energy class from image source
        try:
            energy_class_img = browser.find_element(By.XPATH, '/html/body/div/div[6]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]/img').get_attribute('src')
            match = re.search(r'/img/energy/([a-g])-info\.png', energy_class_img, re.IGNORECASE)
            if match:
                return match.group(1).upper()
        except NoSuchElementException:
            pass

        # If both methods fail, return "N/A"
        return "N/A"
    except Exception as e:
        print(f"Error while scraping energy class: {e}")
        return "N/A"


def house_data_scrape(zip_code):
    filename = f"./data/house_data/house_data_{zip_code}.csv"
    visited_urls = load_visited_urls(filename)

    try:
        with open(f"./data/link_data/data_{zip_code}.csv", "r") as file:
            links = file.readlines()
    except Exception as e:
        print(e)
        return
    
    for link in links:
        link = link.strip()
        if not link or link in visited_urls:
            continue
       
        browser.get(link)
        time.sleep(3)
        try:
            address = scrape_address(browser)
            print(address)
            
            if not address:
                continue
            
            stripped_address = address.split(',')[0].strip()
            x, y = get_coordinates(stripped_address, zip_code)

            price = scrape_price(browser)
            print(price)
            if not price:
                continue

            cleaned_price = int(price.replace(".", "").split()[0])
            type = scrape_type(browser)
            print(type)
            if not type:
                continue

            squaremetres = scrape_squaremetres(browser)
            print(squaremetres)
            if not squaremetres:
                continue

            cleaned_squaremetres = int(squaremetres.split()[0])
            price_sqrtmetres = int(int(cleaned_price) / int(cleaned_squaremetres))   

            energy_class = scrape_energy_class(browser)
            print(energy_class)
            if not energy_class:
                continue

            house_data = {
                'Address': address,
                'X': x,
                'Y': y,
                'Price': cleaned_price,
                'Type': type,
                'Size': cleaned_squaremetres,
                'Squaremeter price': price_sqrtmetres,
                'Energy class': energy_class,
                'Url': link
            }

            #print(filename, house_data)
            
            save_to_csv(house_data, filename)

        except Exception as e:
            print(f"Url skipped: {link}")
            print(e)
            continue
    browser.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetches house data from dinGeo")
    parser.add_argument("zip_code", help="Danish zip code to scrappe data with")

    args = parser.parse_args()

    if not args.zip_code:
        print("Please enter a valid zip code")
    else:
        print("Processing")
        house_data_scrape(args.zip_code)
        print("Data has been saved")
