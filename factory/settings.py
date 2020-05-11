import os


# PIPELINES SETTINGS
# Which pipelines to use
FEED_PIPELINE = 'factory.pipelines.feedpipelines.KafkaFeedPipeline'
STREAM_PIPELINE = 'factory.pipelines.streampipelines.KafkaStreamPipeline'

# KAFKA SETTINGS
# Kafka configs for kafka pipelines
BOOTSTRAP_SERVERS = '127.0.0.1:9092'
FEED_TOPIC = 'FEED'
FEED_QUEUE_MAX_SIZE = 5
STREAM_TOPIC = 'STREAM'


# WORKERS SETTINGS
#reasonable to have as many as cpy cores or less
AMOUNT_OF_WORKERS = os.cpu_count()
WORKER_TYPE = 'factory.workers.workers.SampleWorker'

MIDDLEWARES = [
    'factory.middlewares.middlewares.SampleMiddleware',
    'factory.middlewares.middlewares.SampleMiddlewareTwo',
]













