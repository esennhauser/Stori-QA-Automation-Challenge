Feature: suggestion class
  As a test automation engineer,
  I want to look for "Me" and select Mexico
  So that I can verify the suggestion class functionality.

  Background: I am in "Automation Practice" page

  Scenario:  look for and select mexico
      Given we launch browser and go to Automation Practice page
      When  we enter the word 'Me'
      And   we select 'Mexico'
      Then  we can see 'Mexico' is selected