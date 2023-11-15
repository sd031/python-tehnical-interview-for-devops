#pip install docker

import docker

client = docker.from_env()

# Pull an image
image = client.images.pull('alpine', tag='latest')
print(f"Pulled image: {image.id}")

# Run a container
container = client.containers.run('alpine', 'echo hello world', detach=True)
print(f"Started container: {container.id}")

# List running containers
for container in client.containers.list():
    print(f"Running container: {container.id}")

# Stop the container
container.stop()
print(f"Stopped container: {container.id}")
