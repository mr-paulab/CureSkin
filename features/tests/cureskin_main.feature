# Created by mrpau at 12/10/2022
Feature: Tests for CureSkin Main page
  # Enter feature description here


  Scenario: Footer has link to Terms and Conditions
    # Enter Steps here
    Given open cureskin main shopping page
    When click on Terms and Conditions link
    Then verify Terms and Conditions page displays

#  Scenario: Footer has link to Privacy Policy
#    # Enter Steps here
    Given open cureskin main shopping page
    When click on Privacy Policy link
    Then verify Privacy Policy page displays

#  Scenario: Footer has link to Refund Policy
#    # Enter Steps here
    Given open cureskin main shopping page
    When click on Refund Policy link
    Then verify Refund Policy page displays

#  Scenario: Footer has link to Shipping Policy
#    # Enter Steps here
    Given open cureskin main shopping page
    When click on Shipping Policy link
    Then verify Shipping Policy page displays