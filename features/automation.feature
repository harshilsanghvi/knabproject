## Created by Owner at 02/22/2023
@uiautomation
Feature: Verify automation task creation and execution works as expected
  @library
  Scenario: Create a automation task and verify it's successful execution
    Given user opens the board
    When user navigates to create a automation rule
    And user creates rule to add purple label when new card is added
    And user completes automation rule creation
    Then the added purple color label is displayed on the Rules page

  @library
  Scenario: Create a card and verify successful execution of automation rule
    Given user opens the board
    When user creates a new card on the board with description This is new card
    Then A purple color label is added in the card automatically

  @library
  Scenario: Remove the rule created
    Given user opens the board
    When user navigates to create a automation rule
    When user deletes the purple label rule added
    Then the rule is successfully removed
