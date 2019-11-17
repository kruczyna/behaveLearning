Feature: Login

    Background:
      Given I land on home screen


    Scenario: I want to navigate to Sign In page
      Given I click main Sign In button
      Then I am on SIGN IN page

    Scenario: I want to login via valid credentials
      Given I click main Sign In button
      And I am on SIGN IN page
      And I input "v.k@mail.com" in email field
      And I input "test1234" in password field
      When I click Sign In button
      Then I am a logged in user

    Scenario: I want to log out
      Given I click Sign Out button
      Then I land on home screen

    Scenario: I dont want to login via invalid credentials
      Given I click main Sign In button
      And I am on SIGN IN page
      And I input "mail@mail.com" in email field
      And I input "invalid_password" in password field
      When I click Sign In button
      Then I see form error
