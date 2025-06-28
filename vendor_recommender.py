import json
from datetime import datetime

# Load mock data
with open('mock_data/vendors.json') as f:
    vendors = json.load(f)

with open('mock_data/sample_inputs.json') as f:
    user_input = json.load(f)

# Break down user input
event_type = user_input["event_type"]
budget = user_input["budget"]
location = user_input["location"]
guest_count = user_input["guest_count"]
event_date = user_input["event_date"]

# Budget Allocation (basic logic)
budget_split = {
    "venue": 0.5 * budget,
    "caterer": 0.3 * budget,
    "decorator": 0.2 * budget
}

# Score Vendors
def score_vendor(vendor, category):
    price = vendor["price"]
    if category == "caterer":
        price *= guest_count  # per plate

    # Budget Fit: 1 (under), 0.5 (slightly over), 0 (too costly)
    budget_fit_score = 1 if price <= budget_split[category] else 0.5 if price <= 1.2 * budget_split[category] else 0

    # Location match
    location_score = 1 if vendor["location"].lower() == location.lower() else 0

    # Availability
    availability_score = 1 if event_date in vendor["available_dates"] else 0

    # Rating normalization (out of 5)
    rating_score = vendor["rating"] / 5

    # Final weighted score
    total_score = 0.3 * budget_fit_score + 0.2 * location_score + 0.2 * availability_score + 0.3 * rating_score
    return total_score

# Get top 3 vendors per category
def get_top_vendors(category):
    filtered = [v for v in vendors if v["type"] == category]
    scored = [{"vendor": v, "score": score_vendor(v, category)} for v in filtered]
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:3]

# Generate Recommendations
recommendations = {
    "venue": get_top_vendors("venue"),
    "caterer": get_top_vendors("caterer"),
    "decorator": get_top_vendors("decorator")
}

# Timeline Planner
def generate_planner():
    event_month = datetime.strptime(event_date, "%Y-%m-%d").month
    planner = [
        "📍 Book Venue: 3 months before event (e.g., September)",
        "🍽️ Finalize Caterer: 2 months before (e.g., October)",
        "🌸 Hire Decorator: 1 month before (e.g., November)"
    ]
    return planner

# Output
print("🎉 Smart Vendor Recommendations\n")
for category, items in recommendations.items():
    print(f"Top {category.title()} Options:")
    for item in items:
        v = item["vendor"]
        print(f"- {v['name']} | ₹{v['price']} | Rating: {v['rating']} | {v['location']} | Score: {round(item['score'], 2)}")
    print()

print("📆 Event Planning Timeline:")
for step in generate_planner():
    print(step)
