current_users = ['neal', 'anna', 'admin', 'robin', 'fancy']
new_users = ['neal', 'anna', 'tiffany', 'mindy', 'fancy']

current_users_low = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_low:
		print("This name " + new_user + " is taken.")
	else:
		print("This name " + new_user + " is available.")
