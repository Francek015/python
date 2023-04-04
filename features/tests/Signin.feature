# Created by sfrog at 2023-02-20
Feature: Test Scenario for order sign in

#  Scenario: User gets prompt to sign in in when logged out
#    Given Open Amazon page
#    When Click Orders into search field
#    When Verify Sign in is shown
#    Then verify input field shown


  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present

