##### Edited by David R.


This script is used in a school context, to change an user password on a IDM server, with ldaps protocol.

### Requirements

- Python 3 < 
- Pip3
- Ldap3 package
- Certificate to authentication on ldap server
- User with sufficients privileges to connect on server and change user's password  


### Usage

	1 - Clone this repo on your laptop/server and adapt a secrets file with your environement.
	2 - To update a user password, execute this command in terminal:
		python3 <path_to_script>.update_password.py <user_password> <new_password>

	3 - The password must be succefully updated and valid one time

 
 
