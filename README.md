# Data Engineering - Data Warehouse Tech Stack with PostgreSQL, DBT, and Airflow

## Project Overview

This project aims to create a data warehouse for a city traffic department to host vehicle trajectory data extracted by analyzing footage from swarm drones and static roadside cameras. The system uses an Extract Load Transform (ELT) framework with DBT to enable on-demand data transformation.

## Business Need

The city traffic department requires a scalable data warehouse to manage and analyze large volumes of vehicle trajectory data. By leveraging this data warehouse, the department can improve traffic management, enhance safety measures, and optimize traffic flow in congested areas.

## Data

The dataset used in this project is from pNEUMA, an open large-scale dataset containing naturalistic trajectories of half a million vehicles collected by a swarm of drones in the congested downtown area of Athens, Greece.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Data](#data)
- [ELT Process](#elt-process)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Introduction

This project leverages a modern data engineering tech stack including MySQL/PostgreSQL for data storage, DBT for data transformation, and Airflow for workflow orchestration. The goal is to build a scalable and efficient data warehouse that can handle large volumes of vehicle trajectory data and support advanced analytics.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- PostgreSQL
- Apache Airflow
- DBT (Data Build Tool)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/cheronodaisy/data_warehouse_tech_stack.git
    ```
2. Navigate to the project directory:
    ```sh
    cd data_warehouse_tech_stack
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up your database (PostgreSQL) and configure connection settings in Airflow and DBT.

## Data

The dataset used in this project is from pNEUMA, which includes naturalistic trajectories of half a million vehicles collected by a swarm of drones in Athens, Greece. This data is critical for analyzing traffic patterns and improving traffic management strategies.

## ELT Process

The project uses the ELT framework to manage the data pipeline:

- **Extract**- Data is extracted from the source (pNEUMA Dataset).
- **Load** -The extracted data is loaded into the data warehouse (PostgreSQL).
- **Transform** - Data transformation is performed using DBT based on the department's needs.

## Contributing

Contributions from the community are welcome. If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Open a pull request.

## Acknowledgments

- pNEUMA for providing the dataset.

For any questions or support, please contact [jepchumbadaisy96@gmail.com].
