# RabbitMQ
### What it is? 
RabbitMQ is a solid, mature, general purpose message broker
## Primary use
Message queue for communication and integration within, and between applications. For long-running tasks, or when you need to run reliable background jobs.
### License
Open Source: Mozilla Public License
### Written in 
Earlang
### First Version Released	
2007
### Persistence
Persist messages until they are dropped on the acknowledgement of receipt
### Replay
No
### Routing
Supports flexible routing which can return information to a consumer node
### Message Priority
Supported
### Monitoring
Available through a built-in UI
### Language Support 
Most languages are supported
### Secure Authentication
Supports standard authentication and OAuth2

### YUM AND APT PACKAGE MANAGER
You can learn about Yum and Apt package managers in detail from the address I gave.
https://www.baeldung.com/linux/yum-and-apt


### RabbitMQ Listeners
Ports or hostname/pair on which to listen for "plain" AMQP 0-9-1 and AMQP 1.0 connections (without TLS). See the Networking guide for more details and examples.
<br>Default:<br>
`listeners.tcp.default = 5672`
<br>
https://github.com/rabbitmq/rabbitmq-server/blob/master/deps/rabbit/docs/rabbitmq.conf.example
  
