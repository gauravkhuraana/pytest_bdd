Feature: Cucumber Basket
   As a gardener
   i want to carry cucumbers in a basket,
   so that i don't drop them all

@multiple
Scenario Outline: Add Cucumbers to a basket
  Given the basket has "<initial>" cucumbers
  When "<some>" cucumbers are added to the basket
  Then the basket contains "<total>" cucumbers

  Examples: Amounts
  |initial | some |total|
  |2       |4     |6    |
  |0       |3     |3    |
  |5       |5     |10   |

@remove
Scenario: Remove Cucumbers from a basket
  Given the basket has "8" cucumbers
  When "3" cucumbers are removed from the basket
  Then the basket contains "5" cucumbers
