Feature: Navigate to the homepage and assert that the objects there are expected
	Scenario Outline: navigate to the homepage and check for items
		Given I navigate to <homepage>
		Then I see a <URL>

		Examples:
		| homepage							| URL  	|
		| https://cxp.telxl.com				| cxp  	|
		| https://qat1.call-view.com		| qat1 	|
		| https://telxl.call-control.com	| telxl	|

	Scenario Outline: navigate to the homepage and assert elements are there
		Given I navigate to https://cxp.telxl.com
		Then I see <Elements> on the page

		Examples:
		| Elements				|
		| CXP_image				|
        | signin_text			|
        | username_text			|
        | password_text			|
        | forgot_password		|
        | login_button			|
        | single_sign_on_button	|
        | privacy_policy_link	|


	Scenario Outline: login as customer
		Given I navigate to https://qat1.call-view.com
		When I fill in my <username> and <password> and hit enter
		Then I am logged in and my <name> appears top right

		Examples:
		| username			| password			| name					|
		| custusername		| custpassword		| Daves Pizza Service	|
		| resellerusername	| resellerpassword	| DaveReseller			|
