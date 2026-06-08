import torch
import numpy as np
from pathlib import Path
from transformers import BertForSequenceClassification, AutoTokenizer

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models"

model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

model.eval()

labels = [
    "Finance",
    "Healthcare",
    "IT",
    "Sales & Marketing"
]


def predict_sector(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.nn.functional.softmax(
        outputs.logits,
        dim=1
    ).cpu().numpy()[0]

    confidence = float(np.max(probs))

    if confidence < 0.50:
        return "Other / Unknown", confidence

    sector = labels[np.argmax(probs)]

    return sector, confidence