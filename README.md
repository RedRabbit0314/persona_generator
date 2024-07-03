# Project Title

Create Persona Template after crawling data in Namuwiki

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See the deployment section for notes on how to deploy the project on a live system.

### Prerequisites

The things you need before installing the software.

* Python 3.x (myLocal = 3.11.9)
* pip (Python package installer)
* Identifying the Namu Wiki Site

### Installation

A step by step guide that will tell you how to get the development environment up and running.

```
$ git clone https://github.com/RedRabbit0314/persona_generator.git
$ cd persona_generator
$ pip install -r requirements.txt
```

## Usage

python main.py

## Repo Architecture

📦persona_generator
 ┣ 📂124
 ┃ ┗ 📜chromedriver
 ┣ 📂model
 ┃ ┗ 📜model.py
 ┣ 📂output
 ┃ ┗ 📂 STAYC
 ┃ ┃ ┗ 📜persona.txt
 ┣ 📂prompt
 ┃ ┣ 📜prompt.py
 ┃ ┗ 📜request.py
 ┣ 📂utils
 ┃ ┗ 📜scraping.py
 ┣ 📜.gitignore
 ┣ 📜main.py
 ┣ 📜README.md
 ┗ 📜requirements.txt