Feature: Shorten
  Background: Set up data
    Given I empty the "URL" table
    And I create the following URLs:
      | id | original_url                   | key | title         |
      | 1  | https://www.stackoverflow.com/ | a   | StackOverflow |
    
  Scenario: An user sends an url and receives a shortened url
    Given I Set the url "https://www.python.org/" in the request body
    And I Send a POST request to the endpoint /shorten/
    Then I receive a shortened URL
  
  Scenario: An user sends an already registered url and receives its shortened url
    Given I Set the url "https://www.stackoverflow.com/" in the request body
    And I Send a POST request to the endpoint /shorten/
    Then I see the following response data:
      | id | original_url                   | key | short_url             | title         | visit_count |
      | 1  | https://www.stackoverflow.com/ | a   | http://example.com/a/ | StackOverflow | 0           |
    
  Scenario: An user sends an invalid url and receives an error message
    Given I Set the url "$invalid_url$" in the request body
    And I Send a POST request to the endpoint /shorten/
    Then I see the following response data:
      | error       |
      | Invalid URL |
  
  Scenario: An user sends no url and receives an error message
    Given I Send a POST request to the endpoint /shorten/ with no body
    Then I see the following response data:
      | error       |
      | URL needed  |
