# _*_ coding: utf-8 _*_

"""
功能：
"""

from kafka import KafkaConsumer, TopicPartition

# Kafka 服务器地址
bootstrap_servers = 'your_kafka_server'

# 创建消费者实例
consumer = KafkaConsumer(
    'your_topic',
    group_id='your_group_id',
    bootstrap_servers=bootstrap_servers,
    enable_auto_commit=False  # 关闭自动提交偏移量
)

# 获取 topic 下的所有分区
partitions = consumer.partitions_for_topic('your_topic')

# 获取每个分区的最新偏移量
latest_offsets = {}
for partition in partitions:
    tp = TopicPartition('your_topic', partition)
    consumer.assign([tp])
    consumer.seek_to_end(tp)
    latest_offset = consumer.position(tp)
    latest_offsets[partition] = latest_offset

# 获取当前消费的偏移量
current_offsets = {}
for partition in partitions:
    tp = TopicPartition('your_topic', partition)
    current_offset = consumer.position(tp)
    current_offsets[partition] = current_offset

# 获取未消费的消息
unconsumed_messages = {}

for partition in partitions:
    tp = TopicPartition('your_topic', partition)
    unconsumed_messages[partition] = []

    for offset in range(current_offsets[partition], latest_offsets[partition]):
        consumer.seek(tp, offset)
        msg = next(consumer)
        unconsumed_messages[partition].append(msg.value.decode('utf-8'))

print("未消费的消息：", unconsumed_messages)
