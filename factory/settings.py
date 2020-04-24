import sys
import os
from importlib import import_module
from os.path import join, abspath, dirname

# Which pipelines to use
FEED_PIPELINE = 'factory.pipelines.feedpipelines.FeedPipeline'
STREAM_PIPELINE = 'factory.pipelines.streampipelines'

# Kafka configs for kafka pipelines
BOOTSTRAP_SERVERS = ['127.0.0.1:9092']
FEED_TOPIC = 'feed'
STREAM_TOPIC = 'stream'

# validators settings


# workers settings
TASK_QUEUE_LENGHT = '4'












