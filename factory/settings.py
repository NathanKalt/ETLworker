import sys
import os
from importlib import import_module
from os.path import join, abspath, dirname


# Which pipelines to use
FEED_PIPELINE = 'factory.pipelines.feedpipelines.KafkaFeedPipeline'
STREAM_PIPELINE = 'factory.pipelines.streampipelines.KafkaStreamPipeline'

# Kafka configs for kafka pipelines
BOOTSTRAP_SERVERS = ['127.0.0.1:9092']
FEED_TOPIC = 'feed'
STREAM_TOPIC = 'stream'

#validators settings


# workers settings
AMOUNT_OF_WORKERS = '4'












