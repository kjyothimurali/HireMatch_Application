from utils.predictor import predict_sector
from utils.role_predictor import predict_role

text = """
Python developer with SQL,
machine learning and cloud experience.
"""

sector, conf = predict_sector(text)

print(sector, conf)

role, score = predict_role(
    text,
    sector
)

print(role, score)