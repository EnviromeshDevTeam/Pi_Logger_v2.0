Feature: Publish Data to AWS

    Publishes Data to Amazon Web Internet of Things Service

    Scenario: Publish Data to Amazon
        Given Program is Active
        When environment_monitoring feature finishes recording
        Then Publish Data to Amazon Internet of Things Service

    Scenario: IoT Rule Event
        Given Program is Active
        When Data is Published to Amazon
        Then A Rule is activated to send this to a designated Amazon Lambda