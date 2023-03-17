# Created by sfrog at 2023-02-23
Feature: Checking bestsellers page


  Scenario: Verify Bestsellers links
    Given Open Amazon
    When Bestsellers is clicked
    Then Verify 5 links are shown