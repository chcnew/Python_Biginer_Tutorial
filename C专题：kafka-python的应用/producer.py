# -*- coding: utf-8 -*-
import json

from kafkamanager import KafkaManager

if __name__ == '__main__':
    # 生产者
    kafkamanager = KafkaManager()
    kafkamanager.creat_topic()
    send_info = {
        "ttt": 000,
        "kkk": 111
    }
    result = kafkamanager.send_msg(json.dumps(send_info))
    print("kafka_send_msg is: \n{}".format(result))
    # 消费者
    kafkamanager = KafkaManager()
    consumer = kafkamanager.receive_msg()
    topic = "title"  # 根据TopicName消费
    consumer.subscribe(topics=[topic])
    print("Consumer subscribe with {}.".format(topic))
    while True:
        source_data = next(consumer)
        json_info = json.loads(source_data.value.decode("utf-8"))
        print(json_info)
