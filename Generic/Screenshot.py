import datetime

def take_screenshot(driver):
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"../Defects/{date}.png")
