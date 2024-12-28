import asyncio
import datetime
import time
from datetime import datetime  
import pandas as pd
from convert_excel import nlg_transfer_medical_data


class Dubai_Ins:
    def __init__(self, page, df1, df2):
        self.page = page
        self.df1 = df1  
        self.df2 = df2     
        

    def fetch_value(self, key):
        # Fetches the value from df1 where the KEY matches the provided key
        return self.df1[self.df1['KEY'] == key]['VALUE'].iloc[0]
    

    async def fill_company_information(self):
        # Convert Census Data file
        nlg_transfer_medical_data()

        # Click 'SME' button
        await self.page.locator("iframe[name=\"content\"]").content_frame.get_by_role("button", name="SME Quotation").click()

        # Fill Home page details
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#txt_CompanyName").click()
        company_name = self.fetch_value("Company Name")
        print(f"Company Name: {company_name}")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#txt_CompanyName").fill(company_name)
        await asyncio.sleep(1) 

        businesss_nature = self.fetch_value("Businesss Nature")
        print(f"Company Name: {businesss_nature}")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_buisnessNature").select_option(businesss_nature)
        await asyncio.sleep(1) 

        city = self.fetch_value("City")
        print(f"Company Name: {city}")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#txt_location").fill(city)
        await asyncio.sleep(2) 
    
        contatct_person = self.fetch_value("Contatct Person")
        print(f"Company Name: {contatct_person}")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#txt_contactperson").fill(contatct_person)
        await asyncio.sleep(2) 

        contact_number = self.fetch_value("Contact  Number")
        contact_number = str(contact_number) 
        print(f"Company Name: {contact_number}")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#txt_ContactNumber").fill(contact_number)
        await asyncio.sleep(2) 

        email = self.fetch_value("Email")
        print(f"Company Name: {email}")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#txt_email").fill(email)
        await asyncio.sleep(2) 

        # Default Value is New
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_NewRenew").select_option("New")
        await asyncio.sleep(2) 

        effective_from = self.fetch_value("Effective from")
        if isinstance(effective_from, datetime):
            effective_from_str = effective_from.strftime("%A, %B %d, %Y")
        else:
            # If it's not a datetime object, handle or convert here
            effective_from_str = effective_from

        print(f"Effective From: {effective_from_str}")

       
        # Click Next button
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#btn_submit").click()
        await asyncio.sleep(2) 

#       ------------------------------------------Upload Member List Page------------------------------------

        file_upload_locator = self.page.locator("iframe[name=\"content\"]").content_frame.locator("#fileUpload_member")
        try:
            await asyncio.sleep(2)
            await file_upload_locator.wait_for(state="visible", timeout=15000)
            await file_upload_locator.set_input_files("D:\\AlgoSpring\\python\\DubaiIns\\MemberUpload - Dubaicare.xlsx")
            print("File uploaded successfully")
        except TimeoutError as e:
            print(f"Timeout Error: {e}")
        except Exception as e:
            print(f"Failed to upload file: {e}")

        # click Upload button
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#but_uploadUpload").click()
        await asyncio.sleep(2)

        # Click Next button
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#btn_submit").click()
        await asyncio.sleep(3)

#       -----------------------------------------TOB Page------------------------------------------------------

        # effective_from = self.fetch_value("Effective from")
        # print(f"Company Name: {effective_from}")
        # eff = "Wednesday, December 18, 2024"
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#img_sscal").click()
        await self.page.locator("iframe[name=\"content\"]").content_frame.get_by_title(effective_from_str).click()
        await asyncio.sleep(7)