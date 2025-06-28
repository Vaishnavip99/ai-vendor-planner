# ai-vendor-planner
# Smart Vendor Recommender & Event Planner 🤖🎉

## 📌 Overview

This project was built as part of **Round 1 of the AI Developer Internship at UtsavAi**. It simulates a basic AI system that:

- Accepts user input: event type, budget, location, guest count, and date
- Recommends the most suitable **vendors** (venue, caterer, decorator)
- Suggests a **planning timeline** for the event
- Uses **mock data only**, with no external AI APIs

> Note: This is a **concept demo**, not a production-ready system. The logic is designed to reflect how a real AI assistant might work in a simplified event planning context.

## 🔧 Tech Used
- Python (core logic)
- JSON (mock input/output data)
- Basic AI-style scoring logic (custom)
- Optional: Flowchart created using draw.io or Canva

## 📥 Input (sample_inputs.json)

```json
{
  "event_type": "Wedding",
  "budget": 250000,
  "location": "Pune",
  "guest_count": 200,
  "event_date": "2025-12-20"
}
