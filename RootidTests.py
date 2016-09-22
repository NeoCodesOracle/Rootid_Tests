#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
  Name: Rootid_Tests
  Author: Armando Carmona
  Date: September 12th, 2016
  Description: A small Selenium test suite written in Python to demonstrate
               minimum level proficiency. Test description found in readme.md
'''

import os, sys

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO)

class RootidTests(unittest.TestCase):
  # we need to explicitly declare our target strings as 
  # a unicode string or else our test will fail
  target_phrase = u"jmickela (Jason Mickela) · GitHub"
  target_url_link = u"https://github.com/jmickela"

  def setUp(self):
    '''Initialize browser, sets wait period and maximizes window'''
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()

  def test_jmickela_first_result(self):
    '''Test to ensure target_phrase is first result in Google'''
    try:
      driver = self.driver
      # point browser to google home page
      driver.get('http://www.google.com')
    	# search for the input box
      elem = driver.find_element_by_name('q')
    	# enter search term into box
      elem.send_keys('jmickela github')
      elem.send_keys(Keys.RETURN)
      # every search result is contained exclusively within an h3 tag
      # let's find all of them and put them in a list called elements
      elements = driver.find_elements_by_xpath(
        "//*[@id='rso']/div/div/div/h3/a")

      # this is where we test target_phrase is first result
      self.assertEqual(self.target_phrase, elements[0].text)
      # this is where we test the page links to the expected page
      self.assertEqual(
        self.target_url_link, elements[0].get_attribute('href'))

    finally:
      logging.info("TOTAL RESULTS FROM SEARCH")
      logging.info(len(elements))
      logging.info("PRINTING THE CONTENTS OF THE FIRST ELEMENT")
      logging.info(elements[0].text)
      logging.info("PRINTING THE LINK OF THE FIRST ELEMENT")
      logging.info(elements[0].get_attribute('href'))
      # follow the link of first search result for visual confirmation
      elements[0].click()


if __name__ == "__main__":
    unittest.main()
