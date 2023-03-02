# Created by sfrog at 2023-02-21
Feature: Test Scenario for cart quantity

  Scenario: User clicks cart to check items quantity
    Given Open Amazons page
    When Input Jumanji: The Video Game - Nintendo Switch into search field
    When Open Video Games page
    When Click on item
    When Add to cart
    When Click go to cart
    Then Verify cart has 1 item