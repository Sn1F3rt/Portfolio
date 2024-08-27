# Portfolio

[![Lint](https://github.com/Sn1F3rt/Portfolio/actions/workflows/black.yml/badge.svg)](https://github.com/Sn1F3rt/Portfolio/actions/workflows/black.yml)
[![License](https://img.shields.io/github/license/Sn1F3rt/Portfolio)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/Sn1F3rt/Portfolio)](https://github.com/Sn1F3rt/Portfolio/commits/main/)
[![GitHub stars](https://img.shields.io/github/stars/Sn1F3rt/Portfolio)](https://github.com/Sn1F3rt/Portfolio/)

## Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running](#running)
  - [Development](#development)
  - [Production](#production)
- [Credits](#credits)
- [License](#license)

## About

This repository contains the source code for my personal portfolio website. The application is built using `Quart` and `Jinja2` for the backend and `Bootstrap` for the frontend.

## Prerequisites

- Git
- Python 3.8 or higher (tested on 3.12)

## Installation

1. Clone the repository

   ```shell
    git clone https://github.com/Sn1F3rt/Portfolio.git
   ```
   
2. Switch to the project directory

   ```shell
    cd RoboNerva
   ```
   
3. Create a virtual environment

   ```shell
    python -m venv .venv
   ```
   
4. Activate the virtual environment

   ```shell
    source .venv/bin/activate
   ```
   
5. Install the dependencies

   ```shell
    pip install -r requirements.txt
   ```

## Configuration

Copy the [`config.example.py`](config.example.py) file to `config.py` and update the variables.

## Running

### Development

```shell
python launcher.py
```

### Production

```shell
hypercorn [--certfile <path-to-certificate-file> --keyfile <path-to-key-file> --bind 0.0.0.0:<port>] launcher:app
```

## Credits

Thanks to [@bedimcode](https://github.com/bedimcode/) for the original design idea. 

## License

[Creative Commons Zero v1.0 Universal](LICENSE)

Copyright &copy; 2024 Sayan "Sn1F3rt" Bhattacharyya
