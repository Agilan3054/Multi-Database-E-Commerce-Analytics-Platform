# Multi-Database E-Commerce Analytics Platform

This project involves the development of a comprehensive analytics platform that integrates PostgreSQL for transactional data and MongoDB for product catalog and user activity logs. The platform ensures seamless data integration and provides real-time and historical analytics capabilities.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to provide a unified view of transactional and unstructured data by integrating PostgreSQL and MongoDB. The platform supports real-time analytics to monitor sales, inventory, and user behavior, as well as advanced queries for historical data analysis and user activity insights.

## Features
- Integration of PostgreSQL for transactional data and MongoDB for product catalog and user activity logs.
- Seamless data integration using Python.
- Real-time analytics capabilities.
- Advanced queries for historical data analysis and user activity insights.
- Aggregation queries in MongoDB for flexible data storage.
- Reporting queries in PostgreSQL for structured data analysis.

## Architecture
The platform is designed with the following components:
1. **PostgreSQL**: Used for storing and managing transactional data.
2. **MongoDB**: Used for storing product catalog and user activity logs.
3. **Python Integration**: Ensures seamless data integration between PostgreSQL and MongoDB.
4. **Real-Time Analytics**: Utilizes aggregation queries in MongoDB and reporting queries in PostgreSQL.

## Setup
### Prerequisites
- PostgreSQL
- MongoDB
- Python 3.x
- pip

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/analytics-platform.git
    cd analytics-platform
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up PostgreSQL and MongoDB databases:
    - Create the necessary tables and collections as per the schema definitions.

4. Configure the connection settings in `config.py`:
    ```python
    POSTGRESQL_SETTINGS = {
        'dbname': 'your_dbname',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432',
    }

    MONGODB_SETTINGS = {
        'host': 'localhost',
        'port': '27017',
        'db': 'your_mongodb_dbname',
    }
    ```

## Usage
1. Run the data integration script:
    ```sh
    python data_integration.py
    ```

2. For real-time analytics, execute the relevant scripts to monitor sales, inventory, and user behavior:
    ```sh
    python real_time_analytics.py
    ```

3. For historical data analysis and user activity insights, use the advanced query scripts:
    ```sh
    python historical_data_analysis.py
    ```

## Technologies Used
- **PostgreSQL**: For transactional data storage and reporting queries.
- **MongoDB**: For product catalog and user activity logs.
- **Python**: For data integration and query execution.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.
