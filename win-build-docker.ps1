# Remove existing gunship container
docker rm -f gunship_demo

# Removes any existing gunship_demo images
docker rmi --force gunship_demo

# Build the image from a Dockerfile
docker build --tag=gunship_demo .

# Creates / runs a command on a new container
docker run -p 1555:1555 -dit --name=gunship_demo --rm gunship_demo

