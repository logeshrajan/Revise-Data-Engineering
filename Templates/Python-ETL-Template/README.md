# Python ETL Project Template

A standard template for Python-based ETL projects with best practices and common structure.

## Project Structure

```
project-name/
├── src/
│   ├── __init__.py
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── utils/
├── config/
│   ├── config.yaml
│   └── database.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── docs/
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md
```

## Usage

1. Copy this template to your project directory
2. Rename the project folder appropriately
3. Update requirements.txt with your dependencies
4. Modify configuration files for your data sources
5. Implement your ETL logic in the respective modules

## Features

- Modular ETL architecture
- Configuration management
- Logging setup
- Error handling
- Unit testing framework
- Docker support