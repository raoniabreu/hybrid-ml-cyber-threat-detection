# Hybrid ML Cyber Threat Detection

## Overview
This project demonstrates a hybrid approach combining Machine Learning and rule-based static analysis for cyber threat detection.

## Motivation
Traditional static analysis tools, such as COSSETER, are effective for detecting known vulnerabilities but lack adaptability to evolving threats. Machine learning models, on the other hand, can identify new and unknown attack patterns.

This project combines both approaches.

## Architecture
1. Machine Learning model detects suspicious activity
2. Static analysis module performs deeper inspection

## Technologies
- Python
- Pandas
- Scikit-learn

## Dataset
NSL-KDD dataset

## How to Run
```bash
pip install -r requirements.txt
python main.py
```
## Estructure
```bash
hybrid-ml-cyber-threat-detection/
│
├── data/
├── model/
│   └── train_model.py
├── static_analysis/
│   └── analyzer.py
├── main.py
├── requirements.txt
└── README.md
```

## Autor:

Miqueias Raoni de Abreu