import os


# PIPELINES SETTINGS
# Which pipelines to use
FEED_PIPELINE = 'factory.pipelines.feedpipelines.KafkaFeedPipeline'
STREAM_PIPELINE = 'factory.pipelines.streampipelines.KafkaStreamPipeline'

# KAFKA SETTINGS
# Kafka configs for kafka pipelines
BOOTSTRAP_SERVERS = '127.0.0.1:9092'
FEED_TOPIC = 'FEED'
FEED_QUEUE_MAX_SIZE = os.cpu_count()*2
STREAM_TOPIC = 'STREAM'


# WORKERS SETTINGS
#reasonable to have as many as cpy cores or less
AMOUNT_OF_WORKERS = os.cpu_count()-1
WORKER_TYPE = 'factory.workers.workers.SampleWorker'

MIDDLEWARES = [
    'factory.middlewares.middlewares.SampleMiddleware',
    'factory.middlewares.middlewares.SampleMiddlewareTwo',
]

# LOGGING SETTINGS
LOG_LEVEL = "INFO"










