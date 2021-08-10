# Deployment an Image Classification Deep Learning Model

## What's the problem?
The camera classifies the image incorrectly when classifying it.
## How are images obtained?
Cameras are installed at the facility. The cameras shoot the product from 8 different angles. According to the captured image, the camera gives a result.
## Where is the wrong place?
The most difficult error the camera encounters when grading is the loose wire. So the error is happening on the camera
## Why is there a possibility of misclassification?
Due to the burrs found in the coils, the camera can classify it as loose wire even though there is no loose wire in the image. This is why the camera can misclassify.
## What solution should be implemented?
Images that the camera classifies as loose wire are collected in a pool. Most images in the pool actually turn out to be acceptable burrs. We use deep learning to find out if the images in this repository are faulty. We support the camera with deep learning.

-------------------------------
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
|Language Support| Python, Java, Ruby, PHP, C#, JavaScript, Go, Elixir, Objective-C, Swift, Spring AMQP|Language and Framework Support Kafka APIs support Java and Scala only, but there are many open source (and enterprise solutions) that cover other languages, such as C/C++, Python, . NET, Go, NodeJS, and etc.|Java|
|Secure Authentication|Supports standard authentication and OAuth2|Supports Kerberos, OAuth2, and standard authentication|NiFi supports user authentication via client certificates, via username/password, via Apache Knox, or via OpenId Connect.|


### You can use the links for more detailed information.
For Rabbit MQ : https://www.rabbitmq.com/

For Apache Kafka: https://kafka.apache.org/

For Apache Nifi: https://nifi.apache.org/

---------------------------------------------

### Solution Architect Design
![Copy of Solution Architect Design](https://user-images.githubusercontent.com/88366824/128646043-70513cd9-54a1-4ad3-8b85-493b16a52d6e.png)




