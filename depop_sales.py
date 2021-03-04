#local imports
from creds import e, p

# other imports
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
import pandas as pd
import numpy as np

shops = {
    "always_on_film" : "http://www.depop.com/alwaysonfilm",
    "loaf": "https://www.depop.com/loafcameras/",
    "lensfayre": "https://www.depop.com/lensfayre/",
    "toopshoot": "https://www.depop.com/toopshoot",
    "film_camera_store": "https://www.depop.com/filmcamerastore",
    "retro_camera_shop": "https://www.depop.com/retrocamerashop/",
    "dth_cameras": "https://www.depop.com/dthcameras/"
    }
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

# go onto shops page
# get shop name
# get shops sales
# create a dataframe
# write df to csv
# email csv
class DataframeAndShops(object):

    def __init__(self):
       self.todays_date = datetime.today().date()

    # the start of the shop scraping 

    def aof(self, url):
        self.url = url
        page = requests.get(shops['always_on_film'], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.always_shop_title = soup.find(class_="styles__FullName-aljd70-3 bDDBuZ").text
        self.always_shop_sales = soup.find(class_="Signalstyle__Text-ctceb9-2 cOtrNu").text.strip(" sold")
        
        # need to to function.varName to make it accessible elsewhere
        self.always_shop_summary = f"The shop: {self.always_shop_title} has {self.always_shop_sales} sales on {self.todays_date}"
       
    def loaf(self, url):
        page = requests.get(shops['loaf'], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.loaf_shop_title = soup.find(class_="styles__FullName-aljd70-3 bDDBuZ").text
        self.loaf_shop_sales = soup.find(class_="Signalstyle__Text-ctceb9-2 cOtrNu").text.strip(" sold")

        self.loaf_shop_summary = f"The shop: {self.loaf_shop_title} has {self.loaf_shop_sales} sales on {self.todays_date}"

    def lensfayre(self, url):
        page = requests.get(shops['lensfayre'], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.lensfayre_shop_title = soup.find(class_="styles__FullName-aljd70-3 bDDBuZ").text
        self.lensfayre_shop_sales = soup.find(class_="Signalstyle__Text-ctceb9-2 cOtrNu").text.strip(" sold")

        self.lensfayre_shop_summary = f"The shop: {self.lensfayre_shop_title} has {self.lensfayre_shop_sales} sales on {self.todays_date}"

    def toopshoot(self, url):
        page = requests.get(shops['toopshoot'], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.toopshoot_shop_title = soup.find(class_="styles__FullName-aljd70-3 bDDBuZ").text.strip(" 📸📸")
        self.toopshoot_shop_sales = soup.find(class_="Signalstyle__Text-ctceb9-2 cOtrNu").text.strip(" sold")

        self.toopshoot_shop_summary = f"The shop: {self.toopshoot_shop_title} has {self.toopshoot_shop_sales} sales on {self.todays_date}"

    def film_camera_store(self, url):
        page = requests.get(shops['film_camera_store'], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.fcs_shop_title = soup.find(class_="styles__FullName-aljd70-3 bDDBuZ").text.strip(" 📸📸")
        self.fcs_shop_sales = soup.find(class_="Signalstyle__Text-ctceb9-2 cOtrNu").text.strip(" sold")

        self.fcs_shop_summary = f"The shop: {self.fcs_shop_title} has {self.fcs_shop_sales} sales on {self.todays_date}"
    
    def retro_camera_shop(self, url):
        page = requests.get(shops['retro_camera_shop'], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.retro_cs_shop_title = soup.find(class_="styles__FullName-aljd70-3 bDDBuZ").text.strip(" 📸📸")
        self.retro_cs_shop_sales = soup.find(class_="Signalstyle__Text-ctceb9-2 cOtrNu").text.strip(" sold")

        self.rcs_shop_summary = f"The shop: {self.retro_cs_shop_title} has {self.retro_cs_shop_sales} sales on {self.todays_date}"

    def dth_cameras(self, url):
        page = requests.get(shops['dth_cameras'], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.dth_cameras_shop_title = soup.find(class_="styles__FullName-aljd70-3 bDDBuZ").text.strip(" 📸📸")
        self.dth_cameras_shop_sales = soup.find(class_="Signalstyle__Text-ctceb9-2 cOtrNu").text.strip(" sold")

        self.rcs_shop_summary = f"The shop: {self.dth_cameras_shop_title} has {self.dth_cameras_shop_sales} sales on {self.todays_date}"


    # end of shop scraping, lets build some dataframes

    def create_dataframe(self):
      
        self.data = {
            'Shop Name': [self.always_shop_title, self.loaf_shop_title, self.lensfayre_shop_title,self.toopshoot_shop_title,
            self.fcs_shop_title, self.retro_cs_shop_title, self.dth_cameras_shop_title],

            'Shop Sales': [self.always_shop_sales,self.loaf_shop_sales, self.lensfayre_shop_sales,self.toopshoot_shop_sales,
            self.fcs_shop_sales, self.retro_cs_shop_sales, self.dth_cameras_shop_sales],

            'Date': [self.todays_date, self.todays_date, self.todays_date,self.todays_date,self.todays_date, self.todays_date,self.todays_date]
        }

        self.df = pd.DataFrame(self.data, columns=['Shop Name', 'Shop Sales', 'Date'])


        # we want to find where shop = x
        # find todays sale for that shop 
        # deduct those sales from yesterdays

        return self.df

    def create_csv(self):
        csv = self.df.to_csv('shop_sales.csv', mode='a', index=False, header=False)

    def email_results(self):
        subject= "Daily Depop Summary"
        mailtext = "Subject:"+subject+'\n\n' + str(self.df)
        
        send_from = e
        send_to = "jakedavisphotos@gmail.com"
        try: 
            server = smtplib.SMTP(host="smtp.gmail.com", port=587)
            server.ehlo()
            server.starttls()
            server.login(e, p)
            server.sendmail(send_from, send_to, mailtext)
            print("Email Successfully Sent")
        except:
            print("Email Sending Failed")

# config functions

    # turn email notifications on or off

    def send_email(self, on_or_off):
        if on_or_off == True:
            obj.email_results()
        else:
            pass

    # turn off csv creation

    def create_csv_config(self, on_or_off):
        if on_or_off == True:
            obj.create_csv()
        else:
            pass


obj = DataframeAndShops()


if __name__ == "__main__":
    # shop function calls
    obj.aof(shops['always_on_film'])
    obj.loaf(shops['loaf'])
    obj.lensfayre(shops['lensfayre'])
    obj.toopshoot(shops['toopshoot'])
    obj.film_camera_store(shops['film_camera_store'])
    obj.retro_camera_shop(shops['retro_camera_shop'])
    obj.dth_cameras(shops['dth_cameras'])
    

    # call the dataframe creation
    obj.create_dataframe()

    # config function calls
    obj.send_email(False)
    obj.create_csv_config(True)


