from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#options = webdriver.ChromeOptions()
#options.add_experimental_option("prefs", {
#  "download.default_directory": r"~/Downloads/Test",
#  "download.prompt_for_download": False,
#  "download.directory_upgrade": True,
#  "safebrowsing.enabled": True
#})
#options.add_argument("user-agent="+user_agent_profile)
#driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Firefox()

driver.get("http://www.eni-training.com/client_net/lms_proxy.aspx?Idlng=1&GuidGroup=7dde3948-5344-46ed-95ac-13ae60ec13e7&Method=scorm&xcfgSite=SF%2fg4nmio6OU0962RLlXkA%3d%3d&xcfgBdd=5G7C%2b7ujmaWU%2fCvSYM%2bmLw%3d%3d&xLogin=YXhlbC5naXJhcmQx&xLastName=R0lSQVJE&xFirstName=QXhlbA%3d%3d&GuidDomain=0e89c567-cdcd-4ae6-85e7-3521a24f6fed&LMS_Url=http%3A%2F%2Fmylearningbox.reseau-cd.fr%2Fpluginfile.php%2F76174%2Fmod_scorm%2Fcontent%2F2%2Feniscormres.htm&TypeScore=0&Scorm1_2=0")

delay = 3
try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'LastAccess')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

elem.click()

try:
    elem = WebDriverWait(driver, delay)
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

driver.get('http://www.eni-training.com/client_net/pdfexport.aspx?exporttype=2')
element = driver.find_element_by_id("download")
element.click()

# assert "Python" in driver.title
# elem = driver.find_element_by_id("LastAccess")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
