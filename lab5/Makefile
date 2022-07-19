STATE = app
STATE_TEST = tests
REPO := madvokatov/devops_course

.PHONY: $(STATE)
.PHONY: $(STATE_TEST)

#for some reason the loop is not working and it goes through app only ignoring tests . Will make it manually as I spent 2-3h trying to make it work but it does not .

$(STATE): $(STATE_TEST)
	@docker build -f Dockerfile.$@ -t $(REPO):$@ .
	@echo "image with tag $@ built"

$(STATE_TEST):
	@docker build -f Dockerfile.$@ -t $(REPO):$@ .
	@echo "image with tag $@ built"

run: $(STATE)
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app: $(STATE_TEST)
	@docker run --rm --name test --net=appnet $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

docker-push:
	@echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
	@docker push $(REPO):$(STATE)
	@docker push $(REPO):$(STATE_TEST)

docker-image-remove:
	@docker rmi $$(docker images -a -q) --force
