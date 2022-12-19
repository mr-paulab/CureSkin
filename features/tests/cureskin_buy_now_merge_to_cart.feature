## Created by mrpau at 12/12/2022
  Feature: Test buy now product merged into cart
  Scenario: add product to cart, click buy now for another, view cart to see if 2nd product added
    Given open url for first product
    When click add to cart button
    And open url for second product
    And click buy it now button
    And click cart breadcrumb
    And look for first item in cart
    Then look for second item in cart


