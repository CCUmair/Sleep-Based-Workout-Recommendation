import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import random

# Simulate 500 sleep records
def generate_sample():
    data = []
    for _ in range(500):
        sleep = round(random.uniform(3, 9), 1)
        quality = random.randint(30, 95)
        deep = random.randint(10, 50)

        # Same logic as before
        if sleep < 4:
            label = "Rest"
        elif sleep < 6:
            if quality < 50 or deep < 20:
                label = "Stretching"
            else:
                label = "Light Cardio"
        elif 6 <= sleep <= 8:
            if quality >= 70 and deep >= 25:
                label = "Cardio"
            else:
                label = "Strength"
        elif sleep > 8:
            if quality > 85 and deep > 30:
                label = "HIIT"
            else:
                label = "Strength"
        else:
            label = "Rest"

        data.append([sleep, quality, deep, label])

    df = pd.DataFrame(data, columns=["sleep", "quality", "deep", "label"])
    return df

df = generate_sample()

X = df[["sleep", "quality", "deep"]]
y = df["label"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "workout_model.pkl")
print("Model saved to workout_model.pkl")
