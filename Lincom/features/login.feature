Feature: Login

@test_tc_0_01 
Scenario: Login to page
    When Login application with username: "Karunakar@gomedigo.io" and password: "Oldwine37@"
    Then Verify message show "LOCATION SERVICES"