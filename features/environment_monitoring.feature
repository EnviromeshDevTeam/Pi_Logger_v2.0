Feature: Environment_Monitoring

    Record Information about Environment

    Scenario: Normal Operation Loop
        Given Program is active
        When After 30 seconds of program starting
        Then Record Environment Variables
        And Loop Program
