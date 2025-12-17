from pathlib import Path
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Repo root = parent of scripts/
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# Reproducible randomness
rng = np.random.default_rng(42)

# ---------- Products ----------
categories = ["Electronics", "Home", "Fashion", "Sports", "Beauty", "Books"]
brands = ["Aurum", "NovaTech", "HomeNest", "FlexFit", "Silk&Co", "PageTurner", "GlowLab"]

tag_pool = {
    "Electronics": ["wireless", "bluetooth", "battery", "portable", "noise-cancelling", "4K", "smart"],
    "Home": ["kitchen", "storage", "eco-friendly", "minimal", "durable", "compact", "cleaning"],
    "Fashion": ["casual", "formal", "summer", "winter", "cotton", "leather", "streetwear"],
    "Sports": ["training", "outdoor", "lightweight", "hydration", "grip", "comfort", "performance"],
    "Beauty": ["skincare", "hydrating", "vitamin-c", "sensitive", "fragrance-free", "SPF", "anti-aging"],
    "Books": ["fiction", "non-fiction", "business", "self-help", "science", "history", "fantasy"],
}

def make_desc(cat, tags, brand):
    return f"{brand} {cat.lower()} item designed for {tags[0]} and {tags[1]}. Ideal for everyday use."

products = []
n_products = 60

for pid in range(1, n_products + 1):
    cat = rng.choice(categories)
    brand = rng.choice(brands)
    tags = rng.choice(tag_pool[cat], size=int(rng.integers(3, 6)), replace=False).tolist()
    price = float(np.round(rng.uniform(8, 450), 2))

    products.append({
        "product_id": pid,
        "name": f"{brand} {cat} #{pid}",
        "category": cat,
        "brand": brand,
        "price": price,
        "tags": "|".join(tags),          # stored as pipe-separated
        "description": make_desc(cat, tags, brand),
    })

products_df = pd.DataFrame(products)
products_df.to_csv(DATA_DIR / "sample_products.csv", index=False)

# ---------- Interactions ----------
event_types = ["view", "like", "add_to_cart"]
event_probs = [0.80, 0.15, 0.05]  # most events are views

n_users = 25
n_events = 800
start_ts = datetime(2025, 10, 1, 8, 0, 0)

interactions = []
for eid in range(1, n_events + 1):
    user_id = int(rng.integers(1, n_users + 1))
    product_id = int(rng.integers(1, n_products + 1))
    event_type = rng.choice(event_types, p=event_probs)

    ts = start_ts + timedelta(minutes=int(rng.integers(0, 60 * 24 * 60)))

    interactions.append({
        "event_id": eid,
        "user_id": user_id,
        "product_id": product_id,
        "event_type": event_type,
        "timestamp": ts.isoformat(),
    })

interactions_df = pd.DataFrame(interactions).sort_values("timestamp")
interactions_df.to_csv(DATA_DIR / "sample_interactions.csv", index=False)

print("Created files:")
print("-", DATA_DIR / "sample_products.csv")
print("-", DATA_DIR / "sample_interactions.csv")
