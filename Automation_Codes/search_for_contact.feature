Feature: Search Bar

  Background: common steps
    Given I am logged in
    And I am on the contacts page

  Scenario: Search for a contact by their first name
    When I enter a valid first name in the search bar
    And I click the search button
    Then I should see a list of contacts matching the first name and the list should not contain any contacts with a different first name.

  Scenario:  Search for a contact by their first and last name
    When I enter a valid first name and last name in the search bar
    And I click the search by name button
    Then I should see a list of contacts matching the first and last name and the list should not contain any contacts with a different first or last name

  Scenario: Search for a contact by their email address
    When I enter a valid email address in the search bar
    And I click the search by email button
    Then I should see a list of contacts matching the email address and list should not contain any contacts with a different email address

  Scenario: Search for a contact by their phone number
    When I enter a valid phone number in the search bar
    And I click the search by phone button
    Then I should see a list of contacts matching the phone number and the list should not contain any contacts with a different phone number
