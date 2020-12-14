from github import Github

# Print User name, id, location, number of followers and following
# Print Numbe rof repos, repo names, and repo id

def printUserDetails(user):
	print("~~~~User Details~~~~")
	print("Login : " + user.login)
	print("ID : " + str(user.id))
	print("Name : " + user.name)
	print("URL : " + user.url)
	print("Number of Public Repos : " + str(user.public_repos))





def main():
	
	tokenInput = input("Please enter a User Token : \n")
	g = Github(login_or_token=tokenInput)

	user = g.get_user()
	
	printUserDetails(user)

	
	

main()	