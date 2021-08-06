# MISCLASSIFICATION

## Project Name: Misclassification 

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

# Apache Kafka
### What it is?
Apache Kafka is a message bus optimized for high-ingress data streams and replay
### Primary use
A framework for storing, reading (re-reading), and analyzing streaming data. Optimal for
### License
Open Source: Apache License 2.0
### Written in 
Scala (JVM)
### First Version Released	
20011
### Persistence
Persists messages with an option to delete after a retention period 
### Replay
Yes
### Routing
Does not support flexible routing, must be done through separate topics 
### Message Priority
Not supported
### Monitoring
Available through third-party tools such as when deployed on CloudKarafka or through Confluent
### Language Support 
Most languages are supported
### Secure Authentication
Supports Kerberos, OAuth2, and standard authentication
