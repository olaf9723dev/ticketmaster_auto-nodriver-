import asyncio
import nodriver as uc
import json
import pyautogui
import time
URL = "https://www.carjam.co.nz/car/?plate=UA100/" 

async def main():
    browser = await uc.start()
    # cookies = [
    #     {
    #         'name':'ar_debug', 
    #         'value':'1', 
    #         'domain':'.www.google-analytics.com', 
    #         'path':'/', 
    #     },
    #     {
    #         'name':'cjs', 
    #         'value':'5s5unomg4r15ppgo3f9tb3uc7t', 
    #         'domain':'.carjam.co.nz', 
    #         'path':'/', 
    #     },
    #     {
    #         'name':'_ga', 
    #         'value':'GA1.1.1676185411.1720093093', 
    #         'domain':'.carjam.co.nz', 
    #         'path':'/', 
    #     },
    #     {
    #         'name':'_gid', 
    #         'value':'GA1.3.1249612126.1720093093', 
    #         'domain':'.carjam.co.nz', 
    #         'path':'/', 
    #     },
    #     {
    #         'name':'_ga_TBW8NSXQS5', 
    #         'value':'GS1.1.1720093092.1.1.1720094905.40.0.0', 
    #         'domain':'.carjam.co.nz', 
    #         'path':'/', 
    #     },
    #     {
    #         'name':'cjm', 
    #         'value':'OTU1NWUxNzFkZWYyNjdiZTk4NzRkMjYyOGYxY2MyNGE0MDUzN2FmODk0N2MxMTU4ZDE0ZWIyOGNhNzc2MTNjYnw3Y2VlNmFiMzJjNmJjNmMyfDUwNDI2OHwxNzIyNjg2OTAz', 
    #         'domain':'.carjam.co.nz', 
    #         'path':'/', 
    #     },
    #     {
    #         'name':'cf_clearance', 
    #         'value':'URr1xMP88FJ3SgFFMMJh.5j110QY8VbAdmrvAbvF02Y-1720093058-1.0.1.1-C348Jj4F7FUndT.3mIRANGlUkerfCcdxN.imz8FRFj2Vx86hcFJUG8oW3xWHg.LlFZs7FWZI4X2G9TU5aS9bSw', 
    #         'domain':'.carjam.co.nz', 
    #         'path':'/', 
    #     },
    #     {
    #         'name':'_hjSessionUser_2604973', 
    #         'value':'eyJpZCI6IjEyMDkzZTcyLTg1OTAtNTkyYS1iMDA5LTZlZmU5NjQwZWY2ZiIsImNyZWF0ZWQiOjE3MjAwOTMwOTYzNzMsImV4aXN0aW5nIjp0cnVlfQ==', 
    #         'domain':'.carjam.co.nz', 
    #         'path':'/', 
    #     }
    # ]
    # c = CookieParam(name='n',value='v',path='/',domain='google.com')
    # cookies.append(c)
    # await browser.cookies.set_all(cookies)
    page = await browser.get(URL)
    time.sleep(15)
    location = pyautogui.locateOnScreen('checkbox.png', confidence=0.8)
    if location:
       center = pyautogui.center(location)
       pyautogui.click(center)
    else:
       print("Can't find location")

    # await page.wait_for("iframe", timeout=10000)
    # btn1 = await page.find(text="Verify you are human", best_match=True, timeout=1000)
    # btn1 = await page.find('input[type=checkbox]', timeout=10000)
    # page.wait(3)
    # await btn1.mouse_click()
    # cookies = await page.send(cdp.storage.get_cookies())
    # print(cookies)
    # await page.wait_for("")
    await page.wait(10000000)

if __name__ == '__main__':
    uc.loop().run_until_complete(main())

# import pyautogui
# import time

# URL = "https://www.carjam.co.nz/car/?plate=UA100/" 
# time.sleep(5)
# pyautogui.write(URL, interval=0.1)
# pyautogui.press('enter')
# time.sleep(5)
# location = pyautogui.locateOnScreen('checkbox.png', confidence=0.8)
# if location:
#    center = pyautogui.center(location)
#    pyautogui.click(center)
# else:
#    print("Can't find location")