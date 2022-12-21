## Created by mrpau at 12/12/2022
  Feature: Test for CureSkin Main page links to policies
  Scenario Outline: Footer links to policy pages
    Given open main shopping page
    When click on <value>
    Then verify page by <value>
    Examples:
    |value           |
    |Terms of Service|
#    |Refund Policy   |
#    |Privacy Policy  |
#    |Shipping Policy |
