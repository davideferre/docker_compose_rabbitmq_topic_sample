# docker_compose_rabbitmq_topic_sample
**docker_compose_rabbitmq_topic_sample** is an example on how to use docker compose for running a [rabbitmq server](https://www.rabbitmq.com/) and a receiver python script on _'#'_ topic.
## Quick start
With `docker-compose up` you can run the containers.
After running containers you have to create a python 3 virtualenv with [pika](https://pika.readthedocs.io) installed and run the emitter like `python emit_log_topic.py "some.thing" "A topic message"`.
**Rabbitmq** is listening on _5672_ port on _localhost_ and **rabbitmq management web app** is exposed on http://localhost:15672.
