import asyncio
import time
import os

class Categories1:
    def __init__(self, page, df2, cat1):
        self.page = page
        self.df2 = df2

    def get_value(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df2[column_name].values[0])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    async def categories1_information(self):
        
        # TPA
        tpa = self.get_value("TPA")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_tpaben1").select_option(tpa)
        time.sleep(4)

        # Network
        network = self.get_value("Network")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Prod1").select_option(network)
        time.sleep(3)

        # Annual Limit
        annual_limit = self.get_value("Annual Limit")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_AnnualLimitben1").select_option(annual_limit)
        time.sleep(3)

        # Territory
        territory = self.get_value("Territory")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TerritorialCoverELCben1").select_option(territory)
        time.sleep(3)

        # Deductable
        deductable = self.get_value("Deductable")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_dedben1").select_option(deductable)
        time.sleep(5)

        # Network - Defualt
        # op_co_insurance = self.get_value("Op Co Insurance")
        # print(op_co_insurance)
        # await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_copayben1").select_option(op_co_insurance)
        # time.sleep(3)
        # print(op_co_insurance)

        # Limit of Phamacy
        limit_of_phamacy = self.get_value("Limit of Phamacy")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHLimitben1").select_option(limit_of_phamacy)
        time.sleep(3)

        # Medicine
        medicine = self.get_value("Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MedTypeben1").select_option(medicine)
        time.sleep(3)

        # Pharmacy
        pharmacy = self.get_value("Pharmacy")
        try:
            pharmacy = float(pharmacy) * 100
            pharmacy = f"{int(pharmacy)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHCopayben1").select_option(pharmacy)
        time.sleep(3)
        print(f"Final value sent: {pharmacy}")

        # Physio
        physio = self.get_value("Physio")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physioben1").select_option(physio)
        time.sleep(3)

        # Physio CO
        physio_co = self.get_value("Physio Co")
        try:
            physio_co = float(physio_co) * 100
            physio_co = f"{int(physio_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physiocopay1").select_option(physio_co)
        time.sleep(3)
        print(f"Final value sent: {physio_co}")

        # Maternity - Married Females
        married_females = self.get_value("Maternity - Married Females")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Matben1").select_option(married_females)
        time.sleep(3)

        # Maternity - Married Females CO
        married_females_co = self.get_value("Maternity - Married Females CO")
        try:
            married_females_co = float(married_females_co) * 100
            married_females_co = f"{int(married_females_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MatCopayben1").select_option(married_females_co)
        time.sleep(3)
        print(f"married_females_co is : {married_females_co}")

        # Dental
        dental = self.get_value("Dental")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Dentben1").select_option(dental)
        time.sleep(1)

        # Dental CO
        dental_co = self.get_value("Dental CO")
        try:
            dental_co = float(dental_co) * 100
            dental_co = f"{int(dental_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_DentCopayben1").select_option(dental_co)
        time.sleep(3)
        print(f"Denatal CO is : {dental_co}")

        # Optical
        optical = self.get_value("Optical")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Optben1").select_option(optical)
        time.sleep(1)

        # Optical CO
        optical_co = self.get_value("Optical CO")
        try:
            optical_co = float(optical_co) * 100
            optical_co = f"{int(optical_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_OptCopayben1").select_option(optical_co)
        time.sleep(3)
        print(f"Optical CO is : {optical_co}")

        # Life benefit - Death due to any cause
        life_benefit = self.get_value("Life benefit - Death due to any cause")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_lifeLimit1").select_option(life_benefit)             
        time.sleep(1)

        # Repatriation of Mortal remains
        repatriation = self.get_value("Repatriation of Mortal remains")
        print("Repatriation"+ repatriation)
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_RepatriLimit1").select_option(repatriation)           
        time.sleep(1)

        # Telehealth Consultation
        tele_consultation = self.get_value("Telehealth Consultation")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TeleLimit1").select_option(tele_consultation)          
        time.sleep(1)

        # Wellness Package
        wellness_package = self.get_value("Wellness Package")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_WellPa1").select_option(wellness_package)          
        time.sleep(0.5)

        # Assist America
        assist_america = self.get_value("Assist America")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_ISOS1").select_option(assist_america)          
        time.sleep(0.5)

        # Psychiatry
        psychiatry = self.get_value("Psychiatry")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_psch1").select_option(psychiatry)          
        time.sleep(0.5)

        # Alternative Medicine
        alternative_medicine = self.get_value("Alternative Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_alterMedben1").select_option(alternative_medicine)          
        time.sleep(0.5)

        # Click Get Quote
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#btn_quote").click()

        # Download the Quotation
        download_path = 'D:\\AlgoSpring\\python\\DubaiIns'

        # Ensure the download directory exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        try:
            # Wait for the download to start
            async with self.page.expect_download(timeout=120000) as download_info:
                # Click the download button
                await self.page.locator("iframe[name=\"content\"]").content_frame.locator('#btn_submit').click()

                # Wait for the download to complete and save it to the specified path
                download = await download_info.value
                download_path_full = os.path.join(download_path, "quotation1.pdf")
                await download.save_as(download_path_full)
                print(f"Downloaded quotation PDF to: {download_path_full}")

        except asyncio.TimeoutError:
            print("Error: Timeout exceeded while waiting for the download.")
        except Exception as e:
            print(f"Unexpected error during download: {e}")

        await asyncio.sleep(10) 
