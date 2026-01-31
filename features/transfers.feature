Feature: Money Transfers

  Scenario: Incoming transfer increases balance
    Given Account registry is empty
    And I create an account using name: "jan", last name: "kowalski", pesel: "12345678901"
    When I make an incoming transfer of "100.0" to account with pesel "12345678901"
    Then Account with pesel "12345678901" has "balance" equal to "100.0"

  Scenario: Outgoing transfer decreases balance
    Given Account registry is empty
    And I create an account using name: "anna", last name: "nowak", pesel: "98765432101"
    And I make an incoming transfer of "500.0" to account with pesel "98765432101"
    When I make an outgoing transfer of "200.0" from account with pesel "98765432101"
    Then Account with pesel "98765432101" has "balance" equal to "300.0"

  Scenario: Outgoing transfer fails when insufficient funds
    Given Account registry is empty
    And I create an account using name: "biedny", last name: "student", pesel: "11111111111"
    When I make an outgoing transfer of "100.0" from account with pesel "11111111111"
    Then Request fails with status code 422
    And Account with pesel "11111111111" has "balance" equal to "0.0"