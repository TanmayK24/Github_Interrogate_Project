from github import Github

from datetime import datetime


def printUserDetails(user):
	print("~~~~User Details~~~~")
	print("Login : " + user.login)
	print("ID : " + str(user.id))
	print("Name : " + user.name)
	print("URL : " + user.url)
	print("Number of Public Repos : " + str(user.public_repos))


def printRepoDetails(user):
	print("\n~~~~Public Repo Details~~~~")
	for rep in user.get_repos():
		print("Name : " +rep.name)
		print("Created At " + rep.created_at.strftime('%d/%m/%Y'))
		print("URL : " + rep.url +"\n")


def main():
	
	tokenInput = input("Please enter a User Token : \n")
	g = Github(login_or_token=tokenInput)

	user = g.get_user()
	
	printUserDetails(user)

	printRepoDetails(user)
	

main()	
