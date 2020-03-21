Feature: Shorten
  Background: Set up data
    Given I empty the "URL" table
    
  Scenario: An user sends an url and receives a shortened url
    Given I Set the url "https://www.python.org/" in the request body
    And I Send a POST request to the endpoint /shorten/
    Then I receive a shortened URL
  
  Scenario: An user sends an already registered url and receives its shortened url
    Given I Set the url "https://www.stackoverflow.com/" in the request body
    And I Send a POST request to the endpoint /shorten/
    Then I receive a shortened URL
    And I Send a POST request to the endpoint /shorten/
    Then I receive the same shortened URL
    
  Scenario: An user sends an invalid url and receives an error message
    Given I Set the url "$invalid_url$" in the request body
    And I Send a POST request to the endpoint /shorten/
    Then I see the following response data:
      | error       |
      | Invalid URL |
  
  Scenario: An user sends no url and receives an error message
    Given I Send a POST request to the endpoint /shorten/ with no url
    Then I see the following response data:
      | error       |
      | Invalid URL |
