Feature: OrangeHrm Login

  Scenario: Login to OrangeHRM with valid parameters
    Given User launch chrome browser
    When User access the url
    And User enters the username "Admin" and password "admin123"
    And User clicks on login
    And Validate that user able to see the home page


  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given User launch chrome browser
    When User access the url
    And User enters the username "<username>" and password "<password>"
    And User clicks on login
    And Validate that user able to see the home page

    Examples:
      | username | password |
      | Admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin    |