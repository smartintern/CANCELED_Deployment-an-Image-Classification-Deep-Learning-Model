# RabbitMQ
## Operating System Kernel Limits
Most operating systems enforce limits on kernel resources: virtual memory, stack size, open file handles and more. To Linux users these limits can be known as "ulimit limits".

RabbitMQ nodes are most commonly affected by the maximum open file handle limit. Default limit value on most Linux distributions is usually 1024, which is very low for a messaging broker (or generally, any data service).

For more: https://www.rabbitmq.com/configure.html#kernel-limits


### YUM AND APT PACKAGE MANAGER
You can learn about Yum and Apt package managers in detail from the address I gave.
https://www.baeldung.com/linux/yum-and-apt


### RabbitMQ Listeners
Ports or hostname/pair on which to listen for "plain" AMQP 0-9-1 and AMQP 1.0 connections (without TLS). See the Networking guide for more details and examples.
<br>Default:<br>
`listeners.tcp.default = 5672`


### Rabbit MQ Example
https://github.com/rabbitmq/rabbitmq-server/blob/master/deps/rabbit/docs/rabbitmq.conf.example
  
