
def predict_label(value):
    """Return a prediction based on a threshold."""
    return "positive" if value >= 0.5 else "negative"


def get_message():
    return "MLOps CI/CD demo"


if __name__ == "__main__":
    print("Prediction:", predict_label(0.8))
    print(get_message())
