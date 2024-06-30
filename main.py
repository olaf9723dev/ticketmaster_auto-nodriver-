import asyncio
import nodriver as uc

async def main():
    browser = await uc.start()
    page = await browser.get('https://www.ticketmaster.com/')
    
    await page.save_screenshot()
    await page.get_content()
    await page.scroll_down(150)


    
if __name__ == '__main__':
    uc.loop().run_until_complete(main())