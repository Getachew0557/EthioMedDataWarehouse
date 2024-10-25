# EthioMedDataWarehouse

## Overview

The **EthioMedDataWarehouse** project is designed to collect, clean, process, and analyze data related to Ethiopian medical businesses from various online sources like websites and Telegram channels. The project also incorporates object detection using YOLO (You Only Look Once) to enhance data analysis capabilities. The final product is a robust data warehouse that facilitates comprehensive reporting and insights into the Ethiopian medical sector.

## Business Need

This project was initiated by Kara Solutions, a leading data science company with over 50+ data-centric solutions, to build a scalable data warehouse for storing and analyzing Ethiopian medical business data. The data warehouse will support insights on trends and patterns in the medical field by processing data scraped from Telegram channels and web sources. Additionally, object detection using YOLO will be integrated to help identify specific elements within collected image data.

## Key Features

### Data Scraping and Collection Pipeline

- Scrape data from public Telegram channels related to Ethiopian medical businesses using Python packages such as Telethon, Scrapy, and Selenium.
- Collect images for object detection.

### Data Cleaning and Transformation

- Clean and transform raw data using ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) processes.
- Use DBT (Data Build Tool) for data transformation and ensuring data consistency.

### Object Detection with YOLO

- Integrate YOLO for object detection within images collected from Telegram channels.
- Store and analyze object detection data for business insights.

### Data Warehouse Design and Implementation

- Design a scalable data warehouse to support efficient querying and reporting.
- Store cleaned and transformed data in a relational database (PostgreSQL).

### Data Integration and Enrichment

- Enrich scraped data by integrating multiple data sources.
- Implement pipelines to continuously update the data warehouse.

## Tech Stack

- **Python** (Pandas, Telethon, Scrapy, Selenium)
- **YOLO** for Object Detection (TensorFlow, PyTorch, OpenCV)
- **PostgreSQL** for Data Warehouse
- **DBT** for Data Transformation
- **FastAPI** for Exposing APIs
- **Docker** for Containerization
- **SQLAlchemy** for Database Integration
- **Uvicorn** for ASGI Server

## Installation

- Clone the Repository

```bash
git clone https://github.com/yourusername/EthioMedDataWarehouse.git
cd EthioMedDataWarehouse
```

- Install Dependencies

You will need to install the required dependencies for data scraping, processing, and object detection.

```bash
pip install -r requirements.txt
```

- Set Up Database
Make sure you have PostgreSQL installed and create a new database for the project. Update the database.py file with your database credentials.

```bash
CREATE DATABASE med_data_warehouse;
```

- Set Up YOLO Environment
Clone the YOLOv5 repository and install the necessary dependencies.

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

- Running the Project
You can run individual scripts for different tasks (scraping, data processing, etc.) or run the full pipeline end-to-end.

```bash
python src/scraping/telegram_scraper.py
python src/object_detection/yolo_object_detection.py
```

## Project Structure


```bash
├── app/
│   ├── telegram_scraper.py     # Script for scraping Telegram data
│   ├── utils.py                # Helper functions for scraping
│   └── raw_data/               # Directory where raw data is temporarily stored
├── data/
│   ├── dbt_project/            # DBT models for data transformation
│   └── cleaning_pipeline.py    # Script for running DBT data cleaning models
├── images/
│   ├── detect.py               # Script for YOLO object detection
│   └── images/                 # Scraped images for object detection           # Data
├── logs/
│   ├── main.py                 # FastAPI app entry point
│   ├── crud.py                 # CRUD operations for API
│   ├── schemas.py              # Pydantic schemas for request/response validation
│   └── database.py             # Database connection for FastAPI
│   └── models.py               # SQLAlchemy models for the data warehouse
│   └── database.py             
├── medical_data/
│   ├── telegram_scraper.py     # Script for scraping Telegram data
│   ├── utils.py                # Helper functions for scraping
│   └── raw_data/               # Directory where raw data is temporarily stored
├── notebooks/
│   ├── dbt_project/            # DBT models for data transformation
│   └── cleaning_pipeline.py    # Script for running DBT data cleaning models
├── scripts/
│   ├── detect.py               # Script for YOLO object detection
│   └── images/                 # Scraped images for object detection           # Data
├── src/
│   ├── main.py                 # FastAPI app entry point
│   ├── crud.py                 # CRUD operations for API
│   ├── schemas.py              # Pydantic schemas for request/response validation
│   └── database.py             # Database connection for FastAPI
│   └── models.py               # SQLAlchemy models for the data warehouse
│   └── database.py 
├── tests/
│   ├── telegram_scraper.py     # Script for scraping Telegram data
│   ├── utils.py                # Helper functions for scraping
│   └── raw_data/               # Directory where raw data is temporarily stored
├── yolov5/
│   ├── dbt_project/            # DBT models for data transformation
│   └── cleaning_pipeline.py
├── .gitignore               
├── requirements.txt
└── README.md                   #
```

## Usage

#### Telegram Channels Scraped
- [DoctorsET](https://t.me/DoctorsET)
- [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
- [Yetenaweg](https://t.me/yetenaweg)
- [EAHCI](https://t.me/EAHCI)
- Additional channels from [https://et.tgstat.com/medicine](https://et.tgstat.com/medicine

#### Setup and Execution

1. **Install Dependencies**:
   ```bash
   pip install telethon
   ```

2. **Telegram Scraping**: Before running, make sure to create a `.env` file with your Telegram API credentials (API ID, API hash, and phone number).
   
   Example `.env` file:
   ```plaintext
   API_ID=your_api_id
   API_HASH=your_api_hash
   PHONE=your_phone_number
   ```
- Run `src/scraping/telegram_scraper.py` to collect data from specified Telegram channels.
3. **Data Cleaning and Transformation**: After scraping, the raw data is cleaned and transformed using **DBT** (Data Build Tool). This process involves removing duplicates, handling missing values, and standardizing formats for easy querying and analysis.
#### Setup and Execution

1. **Install DBT**:
   Install DBT and initialize a new DBT project:
   ```bash
   pip install dbt
   dbt init medical_data
   ```

2. **Define DBT Models**:
   - Define SQL models in the `medical_data/models/` directory for cleaning and transforming data.
   - Sample DBT model file:
     ```sql
     -- models/cleaned_telegram_data.sql
     select
         distinct message_id,
         message_text,
         timestamp::timestamp as message_time,
         channel_name
     from raw_data
     where message_text is not null
     ```

3. **Run DBT Models**:
   Apply the transformations by running the DBT models:
   ```bash
   dbt run
   ```

4. **Testing**:
   Test data quality using DBT's built-in test features:
   ```bash
   dbt test
   ```

### 3. Object Detection using YOLO

#### Description
In this task, we perform **object detection** on the scraped images using **YOLOv5** to detect medical equipment, promotional materials, and other objects related to Ethiopian medical businesses.

#### Setup and Execution

1. **Install YOLO Dependencies**:
   Install PyTorch and YOLOv5:
   ```bash
   pip install torch torchvision
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```

2. **Prepare Images**:
   Place the scraped images from the `images/` folder directory for object detection.

3. **Run YOLO**:
   Run the YOLOv5 object detection script:
   ```bash
   cd yolov5
   python detect.py --weights yolov5s.pt --img 640 --conf 0.5 --source data/images
   ```

4. **Store Detection Results**:
   The detection results (bounding boxes, class labels, and confidence scores) will be saved in a structured format, which will later be loaded into the data warehouse.

### 4. Data Warehouse Design and Implementation

#### Description
The data warehouse stores all the cleaned, transformed, and enriched data, enabling efficient querying and analysis. The data includes textual Telegram posts, image metadata, and YOLO object detection results.

#### Setup and Execution

1. **Install PostgreSQL**:
   Install and configure PostgreSQL, or alternatively, use SQLite for local testing.

2. **Database Models**:
   Define your database schema in `app/models.py` using SQLAlchemy:
   ```python
   from sqlalchemy import Column, Integer, String, ForeignKey
   from sqlalchemy.orm import relationship

   class ImageMetadata(Base):
       __tablename__ = 'image_metadata'
       id = Column(Integer, primary_key=True)
       image_path = Column(String, nullable=False)
       channel_name = Column(String, nullable=False)
       timestamp = Column(String, nullable=False)

   class ObjectDetection(Base):
       __tablename__ = 'object_detection'
       id = Column(Integer, primary_key=True)
       image_id = Column(Integer, ForeignKey('image_metadata.id'))
       bounding_box = Column(String, nullable=False)
       confidence = Column(Float, nullable=False)
       class_label = Column(String, nullable=False)

       image = relationship("ImageMetadata", back_populates="detections")
   ```

3. **Migrate Database**:
   Initialize and migrate the database to create the tables:
   ```bash
   python warehouse/database.py
   ```

## FastAPI for Data Access

#### Description
To expose the processed data via an API, **FastAPI** is used to create RESTful endpoints. These endpoints allow users to query the data warehouse for images, detections, and associated metadata.

#### Setup and Execution

1. **Install FastAPI**:
   ```bash
   pip install fastapi uvicorn
   ```

2. **Create FastAPI Application**:
   - Define routes in `fastapi_app/main.py`:
     
```python
     from fastapi import FastAPI, Depends
     from sqlalchemy.orm import Session
     from .crud import get_detections
     from .database import SessionLocal

     app = FastAPI()

     @app.get("/detections/{image_id}")
     def read_detections(image_id: int, db: Session = Depends(get_db)):
         detections = get_detections(db, image_id=image_id

)
         return detections
```

3. **Run FastAPI**:
   Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API**:
   Visit `http://127.0.0.1:8000/` to explore the automatically generated API documentation.

## Contributing

We welcome contributions! Feel free to submit a pull request or open an issue for any bugs or feature requests.

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contact Information

- **Name: Getachew Getu**
- GitHub: [Getachew0557](https://github.com/Getachew0557)
- Email: [getachewgetu2010@gmail.com](mailto:getachewgetu2010@gmail.com)
- LinkedIn: [Getachew Getu](https://www.linkedin.com/in/getachew-getu-9534041a4)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
