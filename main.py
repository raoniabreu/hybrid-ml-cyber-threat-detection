from model.train_model import train_model
from static_analysis.analyzer import static_analysis

def main():
    print("Training ML model...")
    model, X_test, y_test = train_model()

    print("\nRunning predictions...\n")

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