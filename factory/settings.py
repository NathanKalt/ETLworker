import os


# Which pipelines to use
FEED_PIPELINE = 'factory.pipelines.feedpipelines.KafkaFeedPipeline'
STREAM_PIPELINE = 'factory.pipelines.streampipelines.KafkaStreamPipeline'

# Kafka configs for kafka pipelines
BOOTSTRAP_SERVERS = ['127.0.0.1:9092']
FEED_TOPIC = 'feed'
FEED_QUEUE_MAX_SIZE = 100
STREAM_TOPIC = 'stream'

# WORKERS SETTINGS
#reasonable to have as many as cpy cores or less
AMOUNT_OF_WORKERS = os.cpu_count()


MIDDLEWARES = [

]











