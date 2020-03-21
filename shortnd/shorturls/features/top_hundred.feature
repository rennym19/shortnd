Feature: Top-Hundred
  Background: Set up data
    Given I empty the "URL" table
    And I create the following URLs:
      | id | original_url                   | key | title         | visit_count |
      | 1  | https://www.stackoverflow.com/ | a   | StackOverflow | 41          |
      | 2  | https://www.python.org/        | b   | Python        | 28          |
      | 3  | https://www.github.com/        | c   | GitHub        | 35          |

  Scenario: An user wants to see the top one hundred visited URLs
    Given I send a GET request to the endpoint /top_hundred/
    Then I check the number of urls
