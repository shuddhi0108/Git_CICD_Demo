
def predict_label(value):
    """Return a prediction based on a threshold."""
    return "positive" if value >= 0.5 else "negative"


if __name__ == "__main__":
    print("Prediction:", predict_label(0.8))
