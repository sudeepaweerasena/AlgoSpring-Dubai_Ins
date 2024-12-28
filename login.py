import undetected_playwright as playwright
import time
import io
import asyncio
from twocaptcha import TwoCaptcha
import aiofiles


class Login:
    def __init__(self, page):
        self.page = page

    async def perform_login(self, username: str, password: str):
        # while True:
            try:
                # Go to the login page and wait for it to load
                await self.page.goto("https://dubaicare.dubins.ae/")
                await self.page.wait_for_load_state('networkidle')
                # Click Login button
                await self.page.locator("#btn_quote").click()

                # Enter login credentials
                await self.page.locator("#txt_uname").fill(username)
                await self.page.locator("#txt_pwd").fill(password)

                captcha_image = await self.page.locator("#img").screenshot()

                # Asynchronously write the screenshot to a file
                async with aiofiles.open('captcha.png', 'wb') as file:
                    await file.write(captcha_image)

                # Initialize TwoCaptcha solver
                solver = TwoCaptcha('12054431ec2fc8637b7ca76cd31c9401')

                # Solve the CAPTCHA using the file
                result = await asyncio.to_thread(solver.normal, 'captcha.png')
                captcha_code = result['code']
                print("Captcha Code :", captcha_code)
                # Fill in the CAPTCHA text
                await self.page.locator("#txt_captcha").fill(captcha_code)

                # Wait for the button to be clickable
                # await self.page.locator("#btn_signin").wait_for(state="visible")
                await self.page.locator("#btn_signin").click()
               

                # Explicitly wait for the next page or element to load
                await asyncio.sleep(3)

                # Check if the element is visible to determine success
                if await self.page.locator("iframe[name=\"content\"]").content_frame.get_by_role("button", name="SME Quotation").is_visible():
                    print("Login successful!")
                    return True

                else:
                    print("Retrying CAPTCHA...")
                    await asyncio.sleep(1)  # Wait a bit before retrying
                    return False
         

            except Exception as e:
                print(f"Failed to capture or read CAPTCHA: {e}")
                await asyncio.sleep(3)  # Optionally, wait before retrying on error
