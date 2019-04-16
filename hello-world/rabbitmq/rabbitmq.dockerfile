FROM rabbitmq:3.7.14-management

RUN rabbitmq-plugins enable --offline rabbitmq_management

EXPOSE 15671 15672