# Tehran Securities Exchange Data Streaming Project

## Overview


This project retrieves real-time stock market data from the Tehran Securities Exchange Technology Management Co. (TSETMC) API and streams it using Apache Kafka. The data is cleaned, processed, and saved as JSON files every 5 seconds.
## Setup

### Prerequisites
- Python 3.8+
- Apache Kafka
- Zookeeper
- pip (Python package installer)

### Installation
1. Clone the repository:
    ```bash
   git clone https://github.com/dianaseh/tsetmc-data-streaming.git
   cd tsetmc-data-streaming 
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start Zookeeper and Kafka Server:
    ```bash
    # Start Zookeeper
    zookeeper-server-start.sh /path/to/zookeeper/config/zookeeper.properties

    # Start Kafka
    kafka-server-start.sh /path/to/kafka/config/server.properties
    ```

4. Create the Kafka Topic:
    ```bash
    kafka-topics.sh --create --topic tsetmc --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
    ```

## Usage

### Running the Producer
The producer script fetches data from the TSETMC API and sends it to a Kafka topic every 5 seconds.
```bash
python producer.py
```
### Running the Consumer
The consumer script reads data from the Kafka topic and writes it to JSON files in the raw/ directory.

```bash
python consumer.py
```
## Data Cleaning
Only the relevant fields displayed on the TSETMC market map are retained in the JSON data:

- lSecVal
- lVal30
- lVal18AFC
- pClosing
- pDrCotVal
- zTotTran
- qTotTran5J
- qTotCap
- percent
- priceChangePercent
- hEvenShow


## Contact

If you have any questions, feel free to reach out at [dianaseh004@gmail.com](mailto:your-email@gmail.com).

Diana Naseh