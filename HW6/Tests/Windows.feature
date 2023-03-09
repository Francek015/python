# Created by sfrog at 2023-03-03
Feature: Window Handling

  Scenario: User can open and close Amazon pages
    Given Open amazon T&C page
    When Store original windows
    When Click amazon privacy notice
    When Switch to new window
    Then Verify amazon privacy notice window opened
    Then Close window and switch back to original