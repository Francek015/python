# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input watches into search field
##    And Click on search icon
###    Then Product results for watches are shown


#  Scenario: Verify cart login
#    Given Open Amazon page
#    When Orders clicked
#    Then Verify  Sign in  page opened

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias stripbooks-intl-ship
    When Input watches into search field
    When Click on search icon
    Then Verify books department is selected