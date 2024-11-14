# IPL Match Winning Probability Predictor 🏏

This application predicts the probability of winning for IPL (Indian Premier League) cricket matches based on various inputs related to the ongoing match and historic data. It uses a machine learning model to provide real-time predictions, helping fans and analysts estimate the chances of their favorite team winning.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## 📋 Table of Contents
- [IPL Match Winning Probability Predictor 🏏](#ipl-match-winning-probability-predictor-)
  - [📋 Table of Contents](#-table-of-contents)
  - [Features](#features)
  - [🎯 Demo](#-demo)
    - [Screenshot](#screenshot)
  - [🛠️ Technology Stack](#️-technology-stack)
  - [⚙️ Installation](#️-installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites-1)
    - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
    - [Install Dependencies](#install-dependencies)
  - [🚀 Usage](#-usage)
  - [🤖 Model Description](#-model-description)
  - [🌐 Virtual Environment Setup](#-virtual-environment-setup)
    - [Windows](#windows)
    - [macOS/Linux](#macoslinux)
  - [📄 License](#-license)
  - [Contributors](#contributors)

## Features
- **Team Selection**: Choose batting and bowling teams from all IPL franchises
- **City Selection**: Select the match venue from all IPL host cities
- **Match Statistics Input**: 
  - Current score
  - Overs completed
  - Target score
  - Wickets lost
- **Real-Time Predictions**: Get instant win probability predictions
- **User-Friendly Interface**: Clean and intuitive design using Streamlit
- **Responsive Design**: Works seamlessly on both desktop and mobile devices

## 🎯 Demo
The application is live and can be accessed here:  
[IPL Match Predictor App](https://ipl-match-winning-probability-predictor.onrender.com/)

### Screenshot
![Application Screenshot](https://github.com/user-attachments/assets/e0f4166e-dc8a-445e-b712-fbb180f83ff3)

## 🛠️ Technology Stack
- Python 3.8+
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Logistic Regression

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/ankanmitra2002/IPL-Match-Winning-Probability-Predictor
cd ipl-match-predictor
```
## Installation

### Prerequisites

Make sure you have Python installed on your system. It’s also recommended to set up a virtual environment to manage dependencies.

### Setting Up a Virtual Environment

To create and activate a virtual environment, follow these steps:

1. **Create a virtual environment**:

    ```sh
    python -m venv venv
    ```

2. **Activate the virtual environment**:

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

### Install Dependencies

After activating the virtual environment, install the required packages:

```sh
pip install -r requirements.txt
```

## 🚀 Usage
1. Activate the virtual environment (if not already activated)
2. Run the Streamlit app:
```bash
streamlit run app.py
```
1. Open your web browser and navigate to `http://localhost:8501`

## 🤖 Model Description
The application uses a Logistic Regression model trained on historical IPL match data. The model takes into account various features including:
- Current match situation (score, overs, wickets)
- Teams playing
- Venue
- Historical team performance


## 🌐 Virtual Environment Setup
Detailed steps for setting up a virtual environment:

### Windows
```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Deactivate (when done)
deactivate
```

### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate (when done)
deactivate
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors
- [Ankan Mitra](https://github.com/ankanmitra2002)

---
