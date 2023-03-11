Feature: Create New opportunity

  Scenario: Create a new opportunity with only required fields
    Given I am logged in
    And I am on the Kanban view of the Odoo CRM module
    When I click on the "New" button and enter "New Bakery Order" in the "Opportunity Title" field
    And I click the "Add" button
    Then a new opportunity with the title "New Bakery Order" should be created in the "New" stage of the Kanban view
