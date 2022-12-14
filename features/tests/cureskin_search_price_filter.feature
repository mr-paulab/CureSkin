## Created by mrpau at 12/12/2022
  Feature: Test apply price filter to search results
  Scenario Outline: Price filter link select price range
    Given open search results page
    When click <filter_name> open
    Then enter low value <low_value>
    And enter high value <high_value>
    And click <filter_name> to close price filter
    Examples:
    |filter_name      |low_value       |high_value |
    |Pricefilter      |0.00            |1200.00    |
    |Pricefilter      |325.00          |1200.00    |
    |Pricefilter      |350.00          |750.00     |
    |Pricefilter      |490.00          |490.00     |
    |Pricefilter      |750.00          |350.00     |
