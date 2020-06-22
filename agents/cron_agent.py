import json
import utils.kafka_utils as kafka


KAFKA_OUTPUT_TOPIC='crawling_input'
KAFKA_PRODUCER_SETTINGS={ 
	"group.id": "tie", 
	"bootstrap.servers": 
	"backend.novatrends.me:9092", 
	"default.topic.config": { 
		"auto.offset.reset": "earliest", 
		"delivery.timeout.ms": 30000 
	} 
}

if __name__ == '__main__':
    producer = kafka.build_producer(KAFKA_PRODUCER_SETTINGS)
    kafka.write(producer, KAFKA_OUTPUT_TOPIC, json.dumps({
        "request": {
            "keywords": 'computer science'
        }
    }))      