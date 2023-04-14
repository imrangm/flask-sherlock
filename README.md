# flask-init-mini

This project is a boilerplate for future Flask applications.

Below steps can be executed on any unix like system. I will use ubuntu deployed on
[O'Reilly's sandbox](https://learning.oreilly.com/scenarios/ubuntu-sandbox/9781492062837) (alternatively you could use [Katacoda's playground](https://www.katacoda.com/courses/ubuntu/playground2004)). Once the sandbox/playground is ready, execute instructions specified in below sections.

## Setup SSH key

**This step is option and can be omitted.**

Create ssh key and add it to GitHub's [SSH keys](https://github.com/settings/keys) settings.

```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub
```

## Installation

```bash
# Cloning the source code
git clone https://github.com/ldynia/flask-init-mini.git
cd flask-init-mini

# Building and running docker container
docker build --tag flask-mini --build-arg FLASK_DEBUG=True .
docker run --detach --name flask-app --publish 80:8080 --rm flask-mini
docker ps
```

## API

```bash
curl "http://localhost"
```

## Testing

Unit test

```bash
docker exec flask-app pytest
```

Code coverage

```bash
docker exec flask-app coverage run -m pytest
docker exec flask-app coverage report
```

Stop container

```bash
docker stop flask-app
```
