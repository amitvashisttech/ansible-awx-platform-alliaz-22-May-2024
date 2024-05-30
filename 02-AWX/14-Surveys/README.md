# Surveys

Job types of Run or Check will provide a way to set up surveys in the Job Template creation or editing screens. Surveys set extra variables for the playbook similar to ‘Prompt for Extra Variables’ does, but in a user-friendly question and answer way. Surveys also allow for validation of user input. Click the button to create a survey.

Use cases for surveys are numerous. An example might be if operations wanted to give developers a “push to stage” button they could run without advanced Ansible knowledge. When launched, this task could prompt for answers to questions such as, “What tag should we release?”

Many types of questions can be asked, including multiple-choice questions.

## Create a Survey
To create a survey:
1. Click on the button to bring up the Add Survey window.

Use the ON/OFF toggle button at the top of the screen to quickly activate or deactivate this survey prompt.
2. A survey can consist of any number of questions. For each question, enter the following information:
• Name: The question to ask the user
• Description: (optional) A description of what’s being asked of the user.
• Answer Variable Name: The Ansible variable name to store the user’s response in. This is the variable to be used by the playbook. Variable names cannot contain spaces.
• Answer Type: Choose from the following question types.
– Text: A single line of text. You can set the minimum and maximum length (in characters) for this answer.
– Textarea: A multi-line text field. You can set the minimum and maximum length (in characters) for this answer.
– Password: Responses are treated as sensitive information, much like an actual password is treated. You can set the minimum and maximum length (in characters) for this answer.
– Multiple Choice (single select): A list of options, of which only one can be selected at a time. Enter the options, one per line, in the Multiple Choice Options box.
– Multiple Choice (multiple select): A list of options, any number of which can be selected at a time. Enter the options, one per line, in the Multiple Choice Options box.
– Integer: An integer number. You can set the minimum and maximum length (in characters) for this answer.
– Float: A decimal number. You can set the minimum and maximum length (in characters) for this answer.

3. Once you have entered the question information, click the button to add the question.
4. Return to the left pane to add additional questions.
5. When done, click Save to save the survey
