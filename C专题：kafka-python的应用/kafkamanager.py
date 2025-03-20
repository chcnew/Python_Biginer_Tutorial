# -*- coding: utf-8 -*-

"""
功 能：
"""

import ssl

import kafka
from kafka.admin import NewTopic

from util import Utils


class KafkaManager:
    """kafka管理器"""

    def __new__(cls):
        if not hasattr(KafkaManager, "_instance"):
            KafkaManager._instance = object.__new__(cls)
        return KafkaManager._instance

    def __init__(self):
        self.bootstrap_servers = '1.1.1.1:9093,2.2.2.2:9093'
        self.security_protocol = 'SASL_SSL'
        self.sasl_mechanism = 'PLAIN'
        self.sasl_plain_username = 'STAR_TEST'
        self.sasl_plain_password = 'P3ZdgVC33v'
        self.api_version = (0, 10, 2)
        self.context = ssl.create_default_context()
        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.context.load_verify_locations("phy_ca.crt")
        self.producer = None
        self.consumer = None
        self.local_host = Utils.get_local_host()
        self.topics = ["title"]

    def get_topics(self):
        clustermetadata = kafka.cluster.ClusterMetadata(bootstrap_servers=self.bootstrap_servers)
        all_topic = clustermetadata.topics()
        print("All Topic: {}".format(all_topic))

    def creat_topic(self):
        topic_list = [NewTopic(name=self.topics[0], num_partitions=1, replication_factor=1)]
        kafka_admin = kafka.KafkaAdminClient(bootstrap_servers=self.bootstrap_servers,
                                             sasl_mechanism=self.sasl_mechanism,
                                             ssl_context=self.context,
                                             security_protocol=self.security_protocol,
                                             sasl_plain_username=self.sasl_plain_username,
                                             sasl_plain_password=self.sasl_plain_password,
                                             api_version=self.api_version)
        topic_metadata = kafka_admin.list_topics()
        print("Topic MetaData: {}".format(topic_metadata))
        if self.topics[0] not in topic_metadata:
            kafka_admin.create_topics(new_topics=topic_list, validate_only=False)
        else:
            print('TopicAlreadyExists')

    def send_msg(self, msg):
        """生产者"""
        if self.producer is None:
            self.producer = kafka.KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                                sasl_mechanism=self.sasl_mechanism,
                                                ssl_context=self.context,
                                                security_protocol=self.security_protocol,
                                                sasl_plain_username=self.sasl_plain_username,
                                                sasl_plain_password=self.sasl_plain_password,
                                                api_version=self.api_version)
            if not isinstance(msg, bytes):
                msg = msg.encode('utf-8')
            future = self.producer.send(topic=self.topics[0], value=msg)
            result = future.get(timeout=10)
            return result
        return ""

    def receive_msg(self):
        """消费者"""
        if self.consumer is None:
            self.consumer = kafka.KafkaConsumer(bootstrap_servers=self.bootstrap_servers,
                                                group_id=self.local_host,
                                                sasl_mechanism=self.sasl_mechanism,
                                                ssl_context=self.context,
                                                security_protocol=self.security_protocol,
                                                sasl_plain_username=self.sasl_plain_username,
                                                sasl_plain_password=self.sasl_plain_password,
                                                auto_offset_reset='earliest')
        return self.consumer

    def close(self):
        """清理资源"""
        if self.producer is not None:
            self.producer.close()
            self.producer = None
        if self.consumer is not None:
            self.consumer.close()
            self.consumer = None

