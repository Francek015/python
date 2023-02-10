from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

# driver.get('https://www.amazon.ca/ap/signin?ie=UTF8&ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fap%2Fsignin%3Fopenid.pape.max_auth_age%3D900%26openid.return_to%3Dhttps%253A%252F%252Fwww.amazon.ca%252Fgp%252Fyourstore%252Fhome%253Fpath%253D%25252Fgp%25252Fyourstore%25252Fhome%2526useRedirectOnSuccess%253D1%2526signIn%253D1%2526action%253Dsign-out%2526ref_%253Dnav_AccountFlyout_signout%26openid.assoc_handle%3Dcaflex%26openid.mode%3Dcheckid_setup%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=signin&ignoreAuthState=1&disableLoginPrepopulate=1&ref_=ap_sw_aa')


# driver.find_element(By.ID, 'ap_email').send_keys('sfrogina@hotmail.com')
# driver.find_element(By.ID, 'continue').click()

# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()

# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
# driver.find_element(By.ID, 'auth-fpp-link-bottom').click()

# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
# driver.find_element(By.ID, 'ap-other-signin-issues-link').click()

# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
# driver.find_element(By.ID, 'createAccountSubmit').click()

# driver.find_element(By.XPATH, "//*[contains(@href,'/gp/help/customer/display.html/ref=ap_signin_notification_cond')]").click()

# driver.find_element(By.XPATH, "//*[contains(@href,'/gp/help/customer/display.html/ref=ap_signin_notification_privacy')]").click()





driver.quit()