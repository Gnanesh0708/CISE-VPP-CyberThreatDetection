# CISE_VPP
detection of cyber threats in scada controlled pv network systems using machine learning algorithms 

# 5G-Enabled Virtual Power System Cybersecurity Project

This project aims to enhance the cybersecurity of a 5G-enabled virtual power system through the development and evaluation of advanced machine learning models for intrusion detection. The project involves setting up a robust data pipeline, utilizing Docker for environment management, and exporting transformed data to a PostgreSQL database. Various models, including Isolation Forest, One-Class SVM, Autoencoder, and Variational Autoencoder, were tested for their effectiveness in detecting cyber threats.

## Table of Contents

- [Design and Development of Docker Environment](#design-and-development-of-docker-environment)
- [Setting Up Docker Compose](#setting-up-docker-compose)
- [Data Extraction from MQTT Client](#data-extraction-from-mqtt-client)
- [Data Transformation](#data-transformation)
- [Data Exportation to PostgreSQL](#data-exportation-to-postgresql)
- [Model Testing and Evaluation](#model-testing-and-evaluation)
- [Key Outcomes](#key-outcomes)
- [Images](#images)

## Design and Development of Docker Environment

In this project, a robust Docker environment was established by creating a Dockerfile to set up the base environment using the `mageai/mageai:latest` image. This involved configuring essential environment variables and paths required for the project and defining the necessary dependencies in `requirements.txt`, ensuring they were installed correctly within the Docker container. This setup facilitated a consistent and reproducible development environment.

## Setting Up Docker Compose

To manage multiple services efficiently, a `docker-compose.yml` file was developed. This file orchestrated the services, including `magic` and `postgres`, by configuring the required environment variables for both PostgreSQL and the Mage service. Additionally, local volumes were mapped for persistent data storage and secret management, enabling seamless and secure handling of sensitive information.

## Data Extraction from MQTT Client

A data loader was implemented using the MQTT protocol to extract data streams from the MQTT client. This process involved adding crucial columns such as timestamps, ports, IP addresses, and data length to ensure the completeness and accuracy of the extracted data. This step was fundamental in capturing real-time data for further processing and analysis.

## Data Transformation

A transformation pipeline was developed to clean and format the extracted data. This pipeline converted timestamps to datetime format, handled NaN values, and ensured that all column names adhered to snake_case conventions. The transformation process improved the quality and usability of the data, making it ready for export and analysis.

## Data Exportation to PostgreSQL

A PostgreSQL database was set up using Docker Compose to store the cleaned data. The data was exported to PostgreSQL, with specific configurations for the schema and table names as `cise_vpp` and `dynamic_data`, respectively. This step ensured efficient data storage and retrieval, facilitating further analysis and model evaluation.

## Model Testing and Evaluation

Various intrusion detection models, including Isolation Forest, One-Class SVM, Autoencoder, and Variational Encoder, were built and tested. The performance of these models was evaluated to identify the most effective approach for enhancing cybersecurity in the 5G-enabled virtual power system. This phase was crucial in ensuring the system's resilience against potential cyber threats.

## Key Outcomes

- **Successful Implementation of Data Pipeline:** The project successfully established a robust data pipeline capable of extracting data from MQTT, transforming it, and exporting it to PostgreSQL.
- **Effective Use of Docker and Docker Compose:** Streamlined the development and deployment processes, creating a multi-container application to manage data extraction, transformation, and storage efficiently.
- **Improved Data Quality and Management:** Significantly improved data quality through cleaning and formatting, and efficiently stored the data in PostgreSQL with a well-defined schema.
- **Enhanced Cybersecurity Through Model Evaluation:** Developed and tested multiple intrusion detection models, with the Variational Autoencoder (VAE) demonstrating strong performance.

## Images

### Data Processing Workflow
![Data Processing Workflow](file-h1HoEPrjrBLr2NmUrQTmTT7X)

### Data Pipeline
![Data Pipeline](file-iDxrWZ3rFf0mPGJJKiQinTFw)

### Docker Running with Two Containers
![Docker Running with Two Containers](file-ogdd3dmSShzR7wYUX3qfHkhC)

### Data Loaded into Postgres
![Data Loaded into Postgres](file-h1eYAmSlnv9Z16lmIT19tB6U)

---

### Model Agreement Matrix
| Model               | Isolation_Forest | One_Class_SVM | Autoencoder | Variational_Autoencoder |
|---------------------|------------------|---------------|-------------|-------------------------|
| **Isolation_Forest**       | 1.0              | 0.917197       | 0.872611    | 0.89172                 |
| **One_Class_SVM**          | 0.917197         | 1.0            | 0.917197    | 0.923567                |
| **Autoencoder**            | 0.872611         | 0.917197       | 1.0         | 0.968153                |
| **Variational_Autoencoder**| 0.89172          | 0.923567       | 0.968153    | 1.0                     |

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
