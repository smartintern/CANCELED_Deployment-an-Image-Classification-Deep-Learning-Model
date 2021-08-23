#!/usr/bin/env python
# coding: utf-8

#receive_log_topics.py
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()



from __future__ import division, print_function, absolute_import 
import tflearn 
from tflearn.data_utils import shuffle, to_categorical 
from tflearn.layers.core import input_data, dropout, fully_connected 
from tflearn.layers.conv import conv_2d, max_pool_2d 
from tflearn.layers.estimator import regression 
from tflearn.data_preprocessing import ImagePreprocessing 
from tflearn.data_augmentation import ImageAugmentation 


from tflearn.datasets import cifar10 
(X, Y), (X_test, Y_test) = cifar10.load_data() 
X, Y = shuffle(X, Y) 
Y = to_categorical(Y, 10) 
Y_test = to_categorical(Y_test, 10)


img_prep = ImagePreprocessing() 
img_prep.add_featurewise_zero_center() 
img_prep.add_featurewise_stdnorm()


img_aug = ImageAugmentation() 
img_aug.add_random_flip_leftright() 
img_aug.add_random_rotation(max_angle=25.) 


network = input_data(shape=[None, 32, 32, 3], 
                     data_preprocessing=img_prep, 
                     data_augmentation=img_aug) 
network = conv_2d(network, 32, 3, activation='relu') 
network = max_pool_2d(network, 2) 
network = conv_2d(network, 64, 3, activation='relu') 
network = conv_2d(network, 64, 3, activation='relu') 
network = max_pool_2d(network, 2) 
network = fully_connected(network, 512, activation='relu') 
network = dropout(network, 0.5) 
network = fully_connected(network, 10, activation='softmax') 
network = regression(network, optimizer='adam', 
                     loss='categorical_crossentropy', 
                     learning_rate=0.001)


model = tflearn.DNN(network, tensorboard_verbose=0) 
model.fit(X, Y, n_epoch=50, shuffle=True, validation_set=(X_test, Y_test), 
          show_metric=True, batch_size=96, run_id='cifar10_cnn') 


import pika
import sys
#emit_log_topic.py
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
