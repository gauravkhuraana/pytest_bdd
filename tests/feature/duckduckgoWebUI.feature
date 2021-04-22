@web
Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So i can learn new things and get tasks done

  Background:
    Given the DuckDuckGo home page is displayed

@smallQuery
Scenario: Basic DuckDuckGo Search
  When the user searches for "panda"
  Then the results are shown for "panda"

@bigQuery
Scenario: Lengthy DuckDuckGo Search
  When the user searches for the phrase:
   """
    When in the course
   """
  Then one of the results contains "Declaration of Independence"
