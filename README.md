# Hybrid ML Cyber Threat Detection

## Overview

This project presents a hybrid approach for cyber threat detection by combining Machine Learning and rule-based static analysis techniques inspired by COSSETER.

The goal is to improve detection accuracy while reducing false positives by leveraging both adaptive learning and structured analysis.

---

## Author

**Miqueias Raoni de Abreu**
Computer Science Undergraduate – Faculdade Anhanguera
Aspiring PhD Researcher in AI & Cybersecurity

---

## Motivation

Cybersecurity threats are constantly evolving, making traditional detection approaches insufficient.

* Static analysis is precise but limited to predefined rules
* Machine Learning is adaptive but may produce false positives

This project explores a hybrid solution that combines both approaches.

---

## Architecture

The system follows a hybrid pipeline:

1. **Machine Learning Module**

   * Detects suspicious activity using a Random Forest model
   * Trained on the NSL-KDD dataset

2. **Static Analysis Module**

   * Simulates rule-based analysis inspired by COSSETER
   * Identifies risky behaviors (e.g., execution patterns, permissions)

3. **Hybrid Decision Flow**

```python
if prediction != "normal":
    run_static_analysis()
```

---

## Project Structure

```
hybrid-ml-cyber-threat-detection/
│
├── data/
├── model/
│   └── train_model.py
├── static_analysis/
│   └── analyzer.py
├── docs/
│   ├── paper_en.pdf
│   └── paper_pt.pdf
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

---

## Dataset

This project uses the **NSL-KDD dataset**, a standard benchmark for intrusion detection research.

---

## Results

The Random Forest model achieved:

* **Accuracy:** ~89.7%

### Key Observations:

* Strong overall performance across multiple classes
* Some variation in precision and recall due to dataset complexity
* Expected behavior for multi-class cybersecurity datasets

The results demonstrate that the machine learning model is effective in detecting suspicious patterns and supports the hybrid detection approach.

---

## Research Paper

This project is accompanied by a short research paper:

* 📄 [Read the paper (English)](docs/paper_en.pdf)
* 📄 [Leia o artigo (Português)](docs/paper_pt.pdf)

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## Future Work

* Improve feature engineering
* Explore binary classification (normal vs attack)
* Compare additional models
* Integrate real static analysis tools
* Apply deep learning approaches

---

## Contribution

This project demonstrates how combining Machine Learning and static analysis can improve cybersecurity systems and provides a foundation for further research.

---

## License

This project is intended for academic and research purposes.
