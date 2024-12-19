import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from login import Login
from dubai_Ins import Dubai_Ins
from categories1 import Categories1
from categories2 import Categories2
from categories3 import Categories3

async def main():
    file_path = "D:\\AlgoSpring\\python\\DubaiIns\\DubaiInsurance.xlsx"
    df1 = pd.read_excel(file_path, sheet_name="Sheet1")  # Key-Value
    df2 = pd.read_excel(file_path, sheet_name="Sheet2") 

    # Extract unique categories from df2 directly without conversion
    unique_categories_letters = sorted(df2['Category'].unique().tolist())
    
    print(f"Unique categories in letters: {unique_categories_letters}")
  
    browser = None  # Define `browser` outside the try block
    try:
        async with async_playwright() as playwright:
            # Launch the browser
            browser = await playwright.chromium.launch(headless=False)
            context = await browser.new_context()
            context.set_default_timeout(60000)
            page = await context.new_page()

            # Login and process form
            while True:
                login = Login(page)
                if (await login.perform_login("Supriya", "Supriya-GIB")):
                    new_case = Dubai_Ins(page, df1, df2)
                    await new_case.fill_company_information()

                    # Process categories based on the presence of 'A', 'B', and 'C'
                    if 'A' in unique_categories_letters:
                        if 'B' in unique_categories_letters:
                            if 'C' in unique_categories_letters:
                                # If 'A', 'B', and 'C' are present, execute Categories3
                                cat3 = df2[df2['Category'] == 3]
                                categories3 = Categories3(page, df2, cat3)
                                await categories3.categories3_information()
                            else:
                                # If 'A' and 'B' are present, but not 'C', execute Categories2
                                cat2 = df2[df2['Category'] == 2]
                                categories2 = Categories2(page, df2, cat2)
                                await categories2.categories2_information()
                        else:
                            # If only 'A' is present, execute Categories1
                            cat1 = df2[df2['Category'] == 1]
                            categories1 = Categories1(page, df2, cat1)
                            await categories1.categories1_information()

                    # Wait for completion before closing the browser
                    await asyncio.sleep(3)  # Wait for any pending operations

                    # # Click Get Quote
                    # await page.locator("#btn_quote").click()

                    # # Click Get Quote
                    # await page.locator("#btn_submit").click()

                    break

    finally:
        # Ensure the browser closes properly
        if browser:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
