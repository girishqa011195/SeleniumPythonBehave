Feature: OrangeHRM Logo
  Scenario: Validate the logo on OrangeHRM home page
    Given User launch chrome browser
    When User access the url
    Then Verify that user should able see the logo
    And Close the browser