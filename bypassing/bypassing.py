import asyncio
import nodriver as uc
import pyautogui
import time
URL = "https://www.carjam.co.nz/car/?plate=UA100/" 

async def main():
    browser = await uc.start()
    
    page = await browser.get(URL)
    time.sleep(15)

    location = pyautogui.locateOnScreen('checkbox.png', confidence=0.8)
    if location:
       center = pyautogui.center(location)
       pyautogui.click(center)
    else:
       print("Can't find location")

    await page.wait(10000000)

if __name__ == '__main__':
    uc.loop().run_until_complete(main())
