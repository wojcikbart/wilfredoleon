import time
import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get("https://www.eventim.pl/artist/mks-lublin/")

time.sleep(5)
driver.quit()