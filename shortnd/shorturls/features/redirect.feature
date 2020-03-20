Feature: Redirect
  Background: Set up data
    Given I empty the "URL" table
    And I create the following URLs:
      | id | original_url                   | key | title         |
      | 1  | https://www.stackoverflow.com/ | a   | StackOverflow |

  Scenario: An user clicks a shortened URL
    Given I Click on a shortened url with key "a"
    Then I get redirected to an URL
  
  Scenario: An user clicks an invalid shortened URL
    Given I Click on a shortened url with key "z"
    Then I see the following response data:
      | error         |
      | URL Not Found |
