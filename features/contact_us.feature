Feature: Contact Us

	Background:
		Given I land on home screen
		And I click Contact Us button

	Scenario: I want to go to Contact Us
		Then I am on CONTACT US page

	Scenario: I want to see blank Contact Us form error
		Given I click Send button
		Then I see Invalid email address error
