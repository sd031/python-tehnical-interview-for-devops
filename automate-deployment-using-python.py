#pip install gitpython paramiko

import paramiko
from git import Repo

# Configuration
git_repo_url = 'https://github.com/yourusername/your-repo.git'
local_repo_dir = '/path/to/local/repo'
remote_server_ip = 'your.server.ip'
ssh_user = 'your_ssh_username'
ssh_password = 'your_ssh_password'  # For key-based auth, use key_filename parameter instead
remote_project_dir = '/path/to/remote/project'
server_restart_command = 'sudo systemctl restart your-web-service'

# Clone or pull the latest code from the repository
repo = Repo(local_repo_dir)
if repo.bare:
    print("Cloning repository...")
    repo = Repo.clone_from(git_repo_url, local_repo_dir)
else:
    print("Pulling latest code...")
    repo.git.pull()

# SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(remote_server_ip, username=ssh_user, password=ssh_password)

# Deployment commands
commands = [
    f'cd {remote_project_dir}',
    'git pull',
    'pip install -r requirements.txt',  # If your project has a requirements.txt
    server_restart_command
]

# Execute commands
for command in commands:
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())
    print(stderr.read().decode())

ssh.close()
print("Deployment completed.")
