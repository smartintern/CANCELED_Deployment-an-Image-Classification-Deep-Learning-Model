# RabbitMQ

||Rabbit MQ | Apache Kafka | Nifi
|-------|-------|-------|-------|
|What it is?|RabbitMQ is a solid, mature, general purpose message broker|Apache Kafka is a message bus optimized for high-ingress data streams and replay|NiFi was built to automate the flow of data between systems|
|Primary use|Message queue for communication and integration within, and between applications. For long-running tasks, or when you need to run reliable background jobs.|A framework for storing, reading (re-reading), and analyzing streaming data. Optimal for|NiFi allows the setting of one or more prioritization schemes for how data is retrieved from a queue. The default is oldest first, but there are times when data should be pulled newest first, largest first, or some other custom scheme.|
|License|Open Source: Mozilla Public License|Open Source: Apache License 2.0|Open Soruce: Apache License|
|Written in|Earlang|Scala(JVM)|Java|
|First Version Released|2007|2011|2006|
|Persistence|Persist messages until they are dropped on the acknowledgement of receipt|Persists messages with an option to delete after a retention period|NiFi Registry uses a pluggable flow persistence provider to store the content of the flows saved to the registry.|
|Replay|No|Yes|Yes|
|Routing|Supports flexible routing which can return information to a consumer node|Does not support flexible routing, must be done through separate topics|It has the ability to route FlowFiles based on their Attributes.|
|Message Priority|Supported|Not supported|Supported|
|Monitoring|Available through a built-in UI|Available through third-party tools such as when deployed on CloudKarafka or through Confluent|Available through a built-in UI|
|Language Support| Python, Java, Ruby, PHP, C#, JavaScript, Go, Elixir, Objective-C, Swift, Spring AMQP|Language and Framework Support Kafka APIs support Java and Scala only, but there are many open source (and enterprise solutions) that cover other languages, such as C/C++, Python, . NET, Go, NodeJS, and etc.|JAva|
|Secure Authentication|Supports standard authentication and OAuth2|Supports Kerberos, OAuth2, and standard authentication|NiFi supports user authentication via client certificates, via username/password, via Apache Knox, or via OpenId Connect.|






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
<br>
### Rabbit MQ Example
https://github.com/rabbitmq/rabbitmq-server/blob/master/deps/rabbit/docs/rabbitmq.conf.example
  
