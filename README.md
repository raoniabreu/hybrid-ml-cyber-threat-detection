# Hybrid ML Cyber Threat Detection

## Overview

This project presents a hybrid approach for cyber threat detection by combining Machine Learning and rule-based static analysis techniques inspired by COSSETER.

The goal is to improve detection accuracy while reducing false positives by leveraging both adaptive learning and structured code analysis.

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

This project explores a hybrid solution that combines both approaches to improve reliability and performance.

---

## Architecture

The system follows a hybrid pipeline:

1. **Machine Learning Module**

   * Detects suspicious activity using a trained model (Random Forest)
   * Based on the NSL-KDD dataset

2. **Static Analysis Module**

   * Simulates rule-based analysis inspired by COSSETER
   * Identifies risky behaviors such as:

     * Write permission abuse
     * Execution patterns

3. **Hybrid Decision Flow**

```python
if prediction == "suspicious":
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

---

## Dataset

This project uses the **NSL-KDD dataset**, a standard benchmark for intrusion detection research.

---

## Research Paper

This project is accompanied by a short research paper describing the proposed hybrid approach:

* 📄 [Read the paper (English)](docs/paper_en.pdf)
* 📄 [Leia o artigo (Português)](docs/paper_pt.pdf)

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## Results

The hybrid system works as follows:

* Machine Learning identifies suspicious patterns
* Static analysis validates and refines detection
* Reduces false positives and improves interpretability

---

## Future Work

* Integrate real static analysis tools
* Improve feature extraction
* Apply deep learning models
* Expand to real-world datasets

---

## Contribution

This project demonstrates how combining Machine Learning and static analysis can improve cybersecurity systems, providing a foundation for future research.

---

## License

This project is for academic and research purposes.
