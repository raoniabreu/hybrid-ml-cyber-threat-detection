from model.train_model import train_model
from static_analysis.analyzer import static_analysis

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt


def main():
    print("Training ML model...")
    model, X_test, y_test = train_model()

    print("\nEvaluating model...\n")

    
    y_pred = model.predict(X_test)

    # 📊 Metrics
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # 📈 Graphic
    plt.bar(["Random Forest"], [accuracy])
    plt.title("Model Accuracy")
    plt.ylabel("Accuracy")
    plt.savefig("accuracy.png")
    plt.show()

    print("\n--- Hybrid Analysis ---\n")

    # 🔁 hybrid system start here
    for i in range(5):  # test first 5 samples
        sample = X_test.iloc[i:i+1]
        prediction = model.predict(sample)[0]

        print(f"Sample {i+1} prediction: {prediction}")

        if prediction != "normal":
            print("⚠️ Suspicious activity detected! Running static analysis...")
            result = static_analysis(sample)
            print(result)

        print("-" * 50)


if __name__ == "__main__":
    main()