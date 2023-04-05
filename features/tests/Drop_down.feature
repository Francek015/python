# Created by sfrog at 2023-04-05
Feature: Drop down and Hover

#  Scenario: User clicks drop down and searches for item
#    Given Open Amazon outlet page
#    When Select department by alias aps
#    When Input eggs into search field
#    When Click on search icon
#    Then Search results for "eggs" are shown



  Scenario: User opens url and hovers over Account
    Given Open Amazon product page
    When Hover over account
    Then Verify Your list is present