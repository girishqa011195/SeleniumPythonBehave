Feature: Create the customer in nopcommerce application

  Scenario: Validate create customer in nopcommerce
    Given Launch chrome browser
    When User creates the customer
    Then Verify customer created in application