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
    Then I see the following response data:
      | id | original_url                   | key | short_url       | title         | visit_count |
      | 1  | https://www.stackoverflow.com/ | a   | https://te.st/a | StackOverflow | 41          |
      | 3  | https://www.github.com/        | c   | https://te.st/c | GitHub        | 35          |
      | 2  | https://www.python.org/        | b   | https://te.st/b | Python        | 28          |
