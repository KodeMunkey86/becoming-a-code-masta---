from selenium import webdriver
import datetime
import unittest
from selenium.webdriver.common.keys import Keys


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):

        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        desired_capabilities['version'] = ''
        desired_capabilities['platform'] = 'Windows 8'
        desired_capabilities['name'] = 'Website Testing'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://jhayes:b89520c0-92db-45f5-8305-e86a68fed481@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)

    def test_social_media(self):
        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(10)

        assert "Fundraising" in self.driver.title

        #Start of Social media test

        facebook = self.driver.find_element_by_link_text('Facebook')
        self.assertEqual("http://www.facebook.com/GiftGiveLLC",facebook.get_attribute("href"))

        twitter = self.driver.find_element_by_link_text('Twitter')
        self.assertEqual("http://twitter.com/giftgive1", twitter.get_attribute("href"))

        gplus = self.driver.find_element_by_link_text('Google+')
        self.assertEqual("http://plus.google.com/100777158497033145395?prsrc=3", gplus.get_attribute("href"))

        youtube = self.driver.find_element_by_link_text('YouTube')
        self.assertEqual("http://www.youtube.com/ggivesoftware",youtube.get_attribute("href"))

        pint = self.driver.find_element_by_link_text('Pinterest')
        self.assertEqual("http://pinterest.com/giftgive/", pint.get_attribute("href"))

        link = self.driver.find_element_by_link_text('LinkedIn')
        self.assertEqual("http://www.linkedin.com/company/gift-give-inc-", link.get_attribute("href"))

        rss = self.driver.find_element_by_link_text('Blog')
        self.assertEqual("http://qa-gift-give.herokuapp.com/content", rss.get_attribute("href"))

    #End

    def test_header_links(self):
        #checks all the links on the homepage
        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(2)

        np = self.driver.find_element_by_link_text('Nonprofits')
        np.click()
        self.driver.implicitly_wait(2)
        self.assertEqual ("What Is GiFTgive? | GiFTgive", self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        donors = self.driver.find_element_by_link_text('Donors')
        donors.click()
        self.assertEqual ("Browse | GiFTgive" , self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        price = self.driver.find_element_by_link_text('Pricing')
        price.click()
        self.assertEqual("Pricing | GiFTgive" ,self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        faq = self.driver.find_element_by_link_text('FAQ')
        faq.click()
        self.driver.implicitly_wait(5)
        self.assertEqual("FAQ | GiFTgive", self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        contact = self.driver.find_element_by_link_text('Contact')
        contact.click()
        self.driver.implicitly_wait(5)
        self.assertEqual("Help | GiFTgive", self.driver.title)


    def test_blog(self):

        self.driver.get('http://qa-gift-give.herokuapp.com/content')
        self.driver.implicitly_wait(5)

        self.assertEqual("Blog | GiFTgive", self.driver.title)

    def test_login(self):

        self.driver.get("http:/qa-gift-give.herokuapp.com")
        signin = self.driver.find_element_by_id('login')
        signin.click()

        
        username = self.driver.find_element_by_id('user_email')
        password = self.driver.find_element_by_id('user_password')

        #Invalid Test Case -- Both wrong
        username.send_keys('joe@mail.com')
        password.send_keys('strange')
        password.send_keys(Keys.RETURN)

        try:
            self.driver.find_element_by_id('flash_alert')

        except NoSuchElementException:
            return False
        else:
            return True

        #  Valid email and bad password
        username.send_keys('viewtifulbro86@gmail.com')
        password.send_keys('jdhvkjdbfhdb')
        password.send_keys(Keys.RETURN)

        try:
            self.driver.find_element_by_id('flash_alert')
            self.driver.find_element_by_link_text('Forgot your password?')

        except NoSuchElementException:
            return False
        else:
            return True

        #valid credentials
        username.send_keys('viewtifulbro86@gmail.com')
        password.send_keys('ramone6186')
        password.send_keys(Keys.RETURN)

        try:
            self.assertEqual("Friends of the Disabled | GiFTgive", self.driver.title)
            

        except AssertionError:
            return False
        else:
            return True

    def test_what(self):

        self.driver.get('http://qa-gift-give.herokuapp.com/admin/what')
        logo = self.driver.find_element_by_class_name('header-logo')
        logo.click()

        try:
            assert "Fundraising" in self.driver.title
            
        except AssertionError:
            return False
        else:
            return True
        
        self.driver.get('http://qa-gift-give.herokuapp.com/admin/how')

        driver.find_element_by_id("overview_tab").click()
        self.driver.implicitly_wait(1)
        assert 
        
        driver.find_element_by_id("create_tab").click()
        self.driver.implicitly_wait(1)
        
        driver.find_element_by_id("merchandise_tab").click()
        self.driver.implicitly_wait(1)

        
        driver.find_element_by_id("market_tab").click()
        self.driver.implicitly_wait(1)
        
        driver.find_element_by_id("engage_tab").click() 
        self.driver.implicitly_wait(1)
        
        driver.find_element_by_link_text("Thank You").click()
        self.driver.implicitly_wait(1)
        
        driver.find_element_by_link_text("Learn").click()
        self.driver.implicitly_wait(1)
        
        driver.find_element_by_link_text("Free trial! Get started here").click()
        self.driver.implicitly_wait(1)
        
        driver.find_element_by_link_text("What Is GiFTgive?").click()
        self.driver.implicitly_wait(1)
        

        

        
        


        

                
        

        

        
        

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()












