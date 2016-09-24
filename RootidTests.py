#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename='log.txt', level=logging.INFO)


class RootidTests(unittest.TestCase):
	"""
		A small test suite to demonstrate minimum level proficiency with Selenium
	"""
	target_phrase = u"jmickela (Jason Mickela) · GitHub"
	target_url_link = u"https://github.com/jmickela"

	# a container for putting results in 
	elements = []

	def setUp(self):
		"""
			Initialize browser, sets wait period and maximizes window
		"""
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()

	def test_jmickela_first_result(self):
		"""
			Test to ensure target_phrase is first result in Google
		"""
		try:
			driver = self.driver

			# point browser to google home page
			driver.get("http://www.google.com")

			# search for the input box
			elem = driver.find_element_by_name("q")
			# enter search tem into box
			elem.send_keys("jmickela github")
			elem.send_keys(Keys.RETURN)

			# every search result is contained exclusively within an h3 tag
			self.elements = driver.find_elements_by_xpath("//*[@id='rso']/div/div/div/h3/a")

			# this is where we test target_phrase is first result
			self.assertEqual(self.target_phrase, self.elements[0].text)
			# this is where we test the the link takes us to the expected page
			self.assertEqual(self.target_url_link, self.elements[0].get_attribute("href"))

		finally:
			logging.info("\n")
			logging.info("TEST 'jmickela (Jason Mickela) · GitHub' IS FIRST RESULT")
			logging.info("Total results displayed on first page")
			logging.info(len(self.elements))
			logging.info("Printing the inner html contents for the first result")
			logging.info(self.elements[0].text)
			logging.info("Printing the link to page which first result links to")
			logging.info(self.elements[0].get_attribute("href"))
			logging.info("Link is the same as the target_link")
			logging.info("************ ALL TESTS PASSED ************")
			# follow link of first search result for visual confirmation
			self.elements[0].click()

	def test_verify_link(self):
		"""
			Test to ensure page links to specific page
		"""
		target_link = u"http://www.rootid.in/projects/ella-baker-center"

		try:
			# point browser to rootid homepage
			self.driver.get("http://www.rootid.in")
			# search for the link with the text 'VIEW WORK'
			elem = self.driver.find_element_by_link_text("VIEW WORK")
			# click on that link
			elem.click()
			# let's look for all elements and put them in a list
			self.elements[:] = []  # flush list
			self.elements = self.driver.find_elements_by_css_selector("h2.field-content>a")
			# compare the first link to the target_link
			self.assertEqual(target_link, self.elements[0].get_attribute("href"))

		finally:
			logging.info("\n")
			logging.info("TEST 'http://www.rootid.in/projects/ella-baker-center' IS FIRST RESULT")
			logging.info("Total links linking to works")
			logging.info(len(self.elements))
			logging.info("Printing all links in list")
			for link in self.elements:
				logging.info(link.get_attribute("href"))
			logging.info("************ ALL TESTS PASSED ************")
			# follow link of first result for visual confirmation
			self.elements[0].click()

	def test_all_form_fields_required(self):
		"""
			Test to ensure all form fields in contact form are required
		"""
		try:
			# point browser to rootid homepage
			self.driver.get("http://www.rootid.in")

			# scroll window down to bottom, only for demo purposes
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

			# clicking submit with empty fields on required fields
			# triggers error messages for form fields that are required
			button = self.driver.find_element_by_xpath("//*[@id='hsForm_2cec64cb-09a0-4383-acae-77e77f4da49f']/div/div/input")
			button.submit()

			# search for all error messages
			self.elements[:] = [] # flush list
			self.elements = self.driver.find_elements_by_css_selector("ul.hs-error-msgs")

			# the form has four fields, if list has 4 elements
			# it means all form fields are required
			self.assertTrue(len(self.elements) == 4)

		finally:
			logging.info("\n")
			logging.info("TEST ALL FORM FIEDLS ARE REQUIRED")
			logging.info("Total error messages found on page after empty submit")
			logging.info(len(self.elements))
			logging.info("Listing all error messages")
			for index in range(len(self.elements)):
				logging.info(self.elements[index].get_attribute('innerHTML'))


	def tearDown(self):
		"""
			Shuts down the browser upon test completion
		"""
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()
