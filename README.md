# [API Assignment](https://github.com/thulin82/api-assignment)
## Todo Application based on API backend
### How to use (locally)
####  Build
```bash
docker build -t todoapi .
```
#### Run
```bash
docker run -d -p 8080:80 --name todoapi todoapi
```

### How to use (jenkins/local registry)
#### Set up local registry
```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```
#### Set up Jenkins
```bash
docker run -d -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -p 8090:8080 -p 50000:50000 --name jenkins syve/jenkinsci
```
#### Small fix to Jenkins
```bash
docker exec -it -u root jenkins bash
chgrp docker /var/run/docker.sock
```
#### Build and Push Python image to local registry
```bash
cd Scripts
docker build -t localhost:5000/my-python .
docker push localhost:5000/my-python
cd ..
```
#### Step-by-step instructions
1. Set up Jenkins (plugins needed: basic+MSTest Plugin (for trx test reports))
2. Go to [Test Repo](https://github.com/thulin82/api-assignment-tests) and build and push image to local registry
3. Create pipeline in Jenkins
4. Run the pipeline


© Markus Thulin 2019-