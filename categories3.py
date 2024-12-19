import asyncio
import time
import os

class Categories3:
    def __init__(self, page, df2, cat2):
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
        
    def get_value_catB(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df2[column_name].values[1])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None
        
    def get_value_catC(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df2[column_name].values[2])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    async def categories3_information(self):

        # TPA
        tpa = self.get_value("TPA")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_tpaben31").select_option(tpa)
        time.sleep(4)
        
        # Network
        network = self.get_value("Network")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Prod31").select_option(network)
        time.sleep(3)

        # Annual Limit
        annual_limit = self.get_value("Annual Limit")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_AnnualLimitben31").select_option(annual_limit)
        time.sleep(3)

        # Territory
        territory = self.get_value("Territory")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TerritorialCoverELCben31").select_option(territory)
        time.sleep(3)

        # Deductable
        deductable = self.get_value("Deductable")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_dedben31").select_option(deductable)
        time.sleep(5)

        # Network - Defualt
        # op_co_insurance = self.get_value("Op Co Insurance")
        # print(op_co_insurance)
        # await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_copayben31").select_option(op_co_insurance)
        # time.sleep(3)
        # print(op_co_insurance)

        # Limit of Phamacy
        limit_of_phamacy = self.get_value("Limit of Phamacy")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHLimitben31").select_option(limit_of_phamacy)
        time.sleep(3)

        # Medicine
        medicine = self.get_value("Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MedTypeben31").select_option(medicine)
        time.sleep(3)

        # Pharmacy
        pharmacy = self.get_value("Pharmacy")
        try:
            pharmacy = float(pharmacy) * 100
            pharmacy = f"{int(pharmacy)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHCopayben31").select_option(pharmacy)
        time.sleep(3)
        print(f"Final value sent: {pharmacy}")

        # Physio
        physio = self.get_value("Physio")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physioben31").select_option(physio)
        time.sleep(3)

        # Physio CO
        physio_co = self.get_value("Physio Co")
        try:
            physio_co = float(physio_co) * 100
            physio_co = f"{int(physio_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physiocopay31").select_option(physio_co)
        time.sleep(3)
        print(f"Final value sent: {physio_co}")

        # Maternity - Married Females
        married_females = self.get_value("Maternity - Married Females")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Matben31").select_option(married_females)
        time.sleep(3)

        # Maternity - Married Females CO
        married_females_co = self.get_value("Maternity - Married Females CO")
        try:
            married_females_co = float(married_females_co) * 100
            married_females_co = f"{int(married_females_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MatCopayben31").select_option(married_females_co)
        time.sleep(3)
        print(f"married_females_co is : {married_females_co}")

        # Dental
        dental = self.get_value("Dental")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Dentben31").select_option(dental)
        time.sleep(1)

        # Dental CO
        dental_co = self.get_value("Dental CO")
        try:
            dental_co = float(dental_co) * 100
            dental_co = f"{int(dental_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_DentCopayben31").select_option(dental_co)
        time.sleep(3)
        print(f"Denatal CO is : {dental_co}")

        # Optical
        optical = self.get_value("Optical")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Optben31").select_option(optical)
        time.sleep(1)

        # Optical CO
        optical_co = self.get_value("Optical CO")
        try:
            optical_co = float(optical_co) * 100
            optical_co = f"{int(optical_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_OptCopayben31").select_option(optical_co)
        time.sleep(3)
        print(f"Optical CO is : {optical_co}")

        # Life benefit - Death due to any cause
        life_benefit = self.get_value("Life benefit - Death due to any cause")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_lifeLimit31").select_option(life_benefit)             
        time.sleep(1)

        # Repatriation of Mortal remains
        repatriation = self.get_value("Repatriation of Mortal remains")
        print("Repatriation"+ repatriation)
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_RepatriLimit31").select_option(repatriation)           
        time.sleep(1)

        # Telehealth Consultation
        tele_consultation = self.get_value("Telehealth Consultation")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TeleLimit31").select_option(tele_consultation)          
        time.sleep(1)

        # Wellness Package
        wellness_package = self.get_value("Wellness Package")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_WellPa31").select_option(wellness_package)          
        time.sleep(0.5)

        # Assist America
        assist_america = self.get_value("Assist America")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_ISOS31").select_option(assist_america)          
        time.sleep(0.5)

        # Psychiatry
        psychiatry = self.get_value("Psychiatry")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_psch31").select_option(psychiatry)          
        time.sleep(0.5)

        # Alternative Medicine
        alternative_medicine = self.get_value("Alternative Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_alterMedben31").select_option(alternative_medicine)          
        time.sleep(0.5)


#       ------------------------CAT B------------------------------

         # Network
        network = self.get_value_catB("Network")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Prod32").select_option(network)
        time.sleep(3)

        # Annual Limit
        annual_limit = self.get_value_catB("Annual Limit")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_AnnualLimitben32").select_option(annual_limit)
        time.sleep(3)

        # Territory
        territory = self.get_value_catB("Territory")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TerritorialCoverELCben32").select_option(territory)
        time.sleep(3)

        # Deductable
        deductable = self.get_value_catB("Deductable")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_dedben32").select_option(deductable)
        time.sleep(5)

        # Network - Defualt
        # op_co_insurance = self.get_value_catB("Op Co Insurance")
        # print(op_co_insurance)
        # await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_copayben32").select_option(op_co_insurance)
        # time.sleep(3)
        # print(op_co_insurance)

        # Limit of Phamacy
        limit_of_phamacy = self.get_value_catB("Limit of Phamacy")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHLimitben32").select_option(limit_of_phamacy)
        time.sleep(3)

        # Medicine
        medicine = self.get_value_catB("Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MedTypeben32").select_option(medicine)
        time.sleep(3)

        # Pharmacy
        pharmacy = self.get_value_catB("Pharmacy")
        try:
            pharmacy = float(pharmacy) * 100
            pharmacy = f"{int(pharmacy)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHCopayben32").select_option(pharmacy)
        time.sleep(3)
        print(f"Final value sent: {pharmacy}")

        # Physio
        physio = self.get_value_catB("Physio")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physioben32").select_option(physio)
        time.sleep(3)

        # Physio CO
        physio_co = self.get_value_catB("Physio Co")
        try:
            physio_co = float(physio_co) * 100
            physio_co = f"{int(physio_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physiocopay32").select_option(physio_co)
        time.sleep(3)
        print(f"Final value sent: {physio_co}")

        # Maternity - Married Females
        married_females = self.get_value_catB("Maternity - Married Females")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Matben32").select_option(married_females)
        time.sleep(3)

        # Maternity - Married Females CO
        married_females_co = self.get_value_catB("Maternity - Married Females CO")
        try:
            married_females_co = float(married_females_co) * 100
            married_females_co = f"{int(married_females_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MatCopayben32").select_option(married_females_co)
        time.sleep(3)
        print(f"married_females_co is : {married_females_co}")

        # Dental
        dental = self.get_value_catB("Dental")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Dentben32").select_option(dental)
        time.sleep(1)

        # Dental CO
        dental_co = self.get_value_catB("Dental CO")
        try:
            dental_co = float(dental_co) * 100
            dental_co = f"{int(dental_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_DentCopayben32").select_option(dental_co)
        time.sleep(3)
        print(f"Denatal CO is : {dental_co}")

        # Optical
        optical = self.get_value_catB("Optical")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Optben32").select_option(optical)
        time.sleep(1)

        # Optical CO
        optical_co = self.get_value_catB("Optical CO")
        try:
            optical_co = float(optical_co) * 100
            optical_co = f"{int(optical_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_OptCopayben32").select_option(optical_co)
        time.sleep(3)
        print(f"Optical CO is : {optical_co}")

        # Life benefit - Death due to any cause
        life_benefit = self.get_value_catB("Life benefit - Death due to any cause")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_lifeLimit32").select_option(life_benefit)             
        time.sleep(1)

        # Repatriation of Mortal remains
        repatriation = self.get_value_catB("Repatriation of Mortal remains")
        print("Repatriation"+ repatriation)
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_RepatriLimit32").select_option(repatriation)           
        time.sleep(1)

        # Telehealth Consultation
        tele_consultation = self.get_value_catB("Telehealth Consultation")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TeleLimit32").select_option(tele_consultation)          
        time.sleep(1)

        # Wellness Package
        wellness_package = self.get_value_catB("Wellness Package")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_WellPa32").select_option(wellness_package)          
        time.sleep(0.5)

        # Assist America
        assist_america = self.get_value_catB("Assist America")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_ISOS32").select_option(assist_america)          
        time.sleep(0.5)

        # Psychiatry
        psychiatry = self.get_value_catB("Psychiatry")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_psch32").select_option(psychiatry)          
        time.sleep(0.5)

        # Alternative Medicine
        alternative_medicine = self.get_value_catB("Alternative Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_alterMedben32").select_option(alternative_medicine)          
        time.sleep(0.5)


#       ------------------------CAT C------------------------------

         # Network
        network = self.get_value_catC("Network")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Prod33").select_option(network)
        time.sleep(3)

        # Annual Limit
        annual_limit = self.get_value_catC("Annual Limit")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_AnnualLimitben33").select_option(annual_limit)
        time.sleep(3)

        # Territory
        territory = self.get_value_catC("Territory")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TerritorialCoverELCben33").select_option(territory)
        time.sleep(3)

        # Deductable
        deductable = self.get_value_catC("Deductable")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_dedben33").select_option(deductable)
        time.sleep(5)

        # Network - Defualt
        # op_co_insurance = self.get_value_catC("Op Co Insurance")
        # print(op_co_insurance)
        # await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_copayben33").select_option(op_co_insurance)
        # time.sleep(3)
        # print(op_co_insurance)

        # Limit of Phamacy
        limit_of_phamacy = self.get_value_catC("Limit of Phamacy")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHLimitben33").select_option(limit_of_phamacy)
        time.sleep(3)

        # Medicine
        medicine = self.get_value_catC("Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MedTypeben33").select_option(medicine)
        time.sleep(3)

        # Pharmacy
        pharmacy = self.get_value_catC("Pharmacy")
        try:
            pharmacy = float(pharmacy) * 100
            pharmacy = f"{int(pharmacy)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_PHCopayben33").select_option(pharmacy)
        time.sleep(3)
        print(f"Final value sent: {pharmacy}")

        # Physio
        physio = self.get_value_catC("Physio")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physioben33").select_option(physio)
        time.sleep(3)

        # Physio CO
        physio_co = self.get_value_catC("Physio Co")
        try:
            physio_co = float(physio_co) * 100
            physio_co = f"{int(physio_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Physiocopay33").select_option(physio_co)
        time.sleep(3)
        print(f"Final value sent: {physio_co}")

        # Maternity - Married Females
        married_females = self.get_value_catC("Maternity - Married Females")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Matben33").select_option(married_females)
        time.sleep(3)

        # Maternity - Married Females CO
        married_females_co = self.get_value_catC("Maternity - Married Females CO")
        try:
            married_females_co = float(married_females_co) * 100
            married_females_co = f"{int(married_females_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_MatCopayben33").select_option(married_females_co)
        time.sleep(3)
        print(f"married_females_co is : {married_females_co}")

        # Dental
        dental = self.get_value_catC("Dental")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Dentben33").select_option(dental)
        time.sleep(1)

        # Dental CO
        dental_co = self.get_value_catC("Dental CO")
        try:
            dental_co = float(dental_co) * 100
            dental_co = f"{int(dental_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_DentCopayben33").select_option(dental_co)
        time.sleep(3)
        print(f"Denatal CO is : {dental_co}")

        # Optical
        optical = self.get_value_catC("Optical")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_Optben33").select_option(optical)
        time.sleep(1)

        # Optical CO
        optical_co = self.get_value_catC("Optical CO")
        try:
            optical_co = float(optical_co) * 100
            optical_co = f"{int(optical_co)}%" 
        except ValueError:
            pass

        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_OptCopayben33").select_option(optical_co)
        time.sleep(3)
        print(f"Optical CO is : {optical_co}")

        # Life benefit - Death due to any cause
        life_benefit = self.get_value_catC("Life benefit - Death due to any cause")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_lifeLimit33").select_option(life_benefit)             
        time.sleep(1)

        # Repatriation of Mortal remains
        repatriation = self.get_value_catC("Repatriation of Mortal remains")
        print("Repatriation"+ repatriation)
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_RepatriLimit33").select_option(repatriation)           
        time.sleep(1)

        # Telehealth Consultation
        tele_consultation = self.get_value_catC("Telehealth Consultation")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_TeleLimit33").select_option(tele_consultation)          
        time.sleep(1)

        # Wellness Package
        wellness_package = self.get_value_catC("Wellness Package")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_WellPa33").select_option(wellness_package)          
        time.sleep(0.5)

        # Assist America
        assist_america = self.get_value_catC("Assist America")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_ISOS33").select_option(assist_america)          
        time.sleep(0.5)

        # Psychiatry
        psychiatry = self.get_value_catC("Psychiatry")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_psch33").select_option(psychiatry)          
        time.sleep(0.5)

        # Alternative Medicine
        alternative_medicine = self.get_value_catC("Alternative Medicine")
        await self.page.locator("iframe[name=\"content\"]").content_frame.locator("#ddl_alterMedben33").select_option(alternative_medicine)          
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