Easy to setup and adapt ETL tool 

Its async + multiprocessing so several workers can transform data simultaneously 
Really helpful for Kafka or RabbitMQ  

- write your own pipelines classes for feed and stream and set them in settings (oruse natively provided) 
- write your own worker class or use natively provided and set it in settings.py
- write your own chain of middlewares to transform the data between sources 

 