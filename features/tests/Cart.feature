# Created by sfrog at 2023-02-21
Feature: Test Scenario for cart quantity

  Scenario: User clicks cart to check items quantity
    Given Open Amazons page
    When Click cart icon
    Then Verify Your Amazon Cart is empty is visible