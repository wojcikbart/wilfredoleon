import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.common.keys as Keys


def oscamuj_zbiletow(url, normal_amount=1, relief_amount=1):
    MAX_TICKET_AMOUNT = 8
    TICKET_COUNT = 0

    ticket_amounts = {
        "Normalny": normal_amount,
        "Ulgowy": relief_amount,
    }

    driver = uc.Chrome()
    driver.get(url)
    time.sleep(2)

    wait = WebDriverWait(driver, 15, poll_frequency=0.01)

    accept_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cmpboxbtnyes')))
    accept_button.click()
    print("✅ Clicked 'Ok, zgadzam się' button!")

    while True:
        dodaj_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="continue-button"]')))
        if dodaj_button.text == "Zamów":
            break
        time.sleep(1)
        print("waiting for 'Zamów' button")
        driver.refresh()

    dodaj_button.click()
    print("Clicked 'Zamów' button successfully")

    ticket_types = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-qa="tickettype"]')))

    for ticket_type in ticket_types:

        ticket_title_div = ticket_type.find_element(By.CSS_SELECTOR, '[class="ticket-type-title"]')
        ticket_title = ticket_title_div.text
        
        for ticket_amount_key, ticket_amount_value in ticket_amounts.items():
            if ticket_amount_key.lower() in ticket_title.lower():
                ticket_amount = ticket_amount_value
                break

        print(f"Zamawiam bratku {ticket_amount} biletów typu {ticket_title}")
        more_tickets_button = ticket_type.find_element(By.CSS_SELECTOR, '[data-qa="more-tickets"]')
        for i in range(ticket_amount):
            if TICKET_COUNT >= MAX_TICKET_AMOUNT:
                print("Max ticket amount reached")
                break
            more_tickets_button.click()
            TICKET_COUNT += 1

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="add-to-shopping-cart"]')))
    add_to_cart_button.click()
    print("Przejmujesz stery bratku 😎. Nie spierdol tego plsss!")

    time.sleep(2000)
    driver.quit()


# driver.get("https://www.eventim.pl/artist/mks-lublin/")
# driver.get("https://www.eventim.pl/artist/bogdanka-luk-lublin/")

if __name__ == "__main__":
    url = "https://www.eventim.pl/artist/mks-lublin/"
    oscamuj_zbiletow(url)