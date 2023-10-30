#Andrew is my lecturer. Andrew is, Andrew was and Andrew will forever be, Andrew. His name is not Andrew. Test to see if this txt file will change Andrew to Ger-m "test


from github import Github

# Replace these with your GitHub PAT and repository information
github_token = "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"
repo_owner = "Gerard Ball"
repo_name = "test-repository"
file_path = "sample.py"
your_name = "Ger"  
 
g = Github(github_token)


repo = g.get_user(repo_owner).get_repo(repo_name)


file = repo.get_contents(file_path)

file_content = file.decoded_content.decode("utf-8")

# Replace "Andrew" 
file_content = file_content.replace("Andrew", your_name)

# Commit the changes
repo.update_file(
    file_path,
    f"Replace 'Andrew' with {your_name}",
    file_content,
    file.sha,
)

print("Changes committed and pushed to the repository.")