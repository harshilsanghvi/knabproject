# Created by Owner at 02/22/2023
Feature: Verify if card can be created, read, updated and deleted from the Trello Board

  @library
  Scenario Outline: Verify Create a Card API functionality
    Given the Card details of <name> <desc> <pos> and <due> for Trello Board
    When we execute the Create a Card API method
    Then card is created successfully
    Then status code of response is 200
    Examples:
      | name  | desc  | pos | due |
      | Card1 | Trello1 | 1 | 06/06/2023 |
      | Card2 | Trello2 | 2 | 07/06/2023 |
      | Card3 | Trello3 | 3 | 08/06/2023 |


  @library
  Scenario: Verify Get a Card API functionality
    Given a new Card with Card4 and 08/09/2023 is created in the Trello Board
    And the new card with correct id
    When we execute the Get a Card API method
    Then card details are successfully retrieved
    And  status code of response is 200


  @library
  Scenario: Verify Update a Card API functionality
    Given a new Card with Card5 and 08/10/2023 is created in the Trello Board
    And the new card with correct id
    And updated desc value is Latest Updated
    When we execute the Update a Card API method
    Then card desc is successfully updated
    And  status code of response is 200


  @library
  Scenario: Verify Delete a Card API functionality
    Given a new Card with Card6 and 09/10/2023 is created in the Trello Board
    And the new card with correct id
    When we execute the Delete a Card API method
    Then card details are successfully deleted
    And  status code of response is 200


  @library
  Scenario: Verify Delete a Card API functionality
    Given a card with incorrect id
    When we execute the Delete a Card API method
    Then  status code of response is 400