Feature: Navigate to the homepage and assert that the objects there are expected
	Scenario Outline: navigate to the homepage and check for items
		Given I navigate to <homepage>
		Then I see a <URL>

		Examples:
		| homepage			| URL  |
		| https://cxp.telxl.com		| cxp  |
		| https://qat1.call-view.com	| qat1 |
