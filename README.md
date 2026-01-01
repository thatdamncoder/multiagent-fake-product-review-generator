# Multi-Agent Fake Review Detection System

A **LangGraph-based multi-agent system** that detects fake product reviews in real time using **Google Gemini**. The system runs multiple specialized agents **in parallel** to evaluate reviewer credibility, review content authenticity, and purchase verification, then aggregates their decisions into a final moderation action.

---

## 🚀 Features

* **Parallel Multi-Agent Architecture** using LangGraph
* **Three Specialized Agents**:

  * Reviewer Credibility Agent
  * Review Content Authenticity Agent
  * Purchase Verification Agent
* **Prompt-only intelligence** (no scraping, no databases)
* **Explainable decisions** with confidence scores
* **Easy input modification** via a text file
* Powered by **Google Gemini**

---

## 📁 Project Structure

```
multiagent-fake-product-review-generator/
│
├── main.py            # LangGraph orchestration
├── agents.py          # Gemini-powered agents
├── prompts.py         # Detailed agent prompts
├── input.txt          # User-editable input file
├── requirements.txt   # Python dependencies
└── .env               # Gemini API key (not committed)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

### 2️⃣ Add Gemini API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

> Make sure `.env` is added to `.gitignore`.

---

### 3️⃣ Modify Input (Optional)

Edit `input.txt` to test different review scenarios:

```txt
[REVIEWER_INFO]
Account age: 0 days
Past reviews: 0
Verified buyer: NO

[REVIEW_TEXT]
Terrible headphones. Sound quality is bad.

[PURCHASE_INFO]
Purchase found: NO
Review posted same day
```

No code changes are required.

---

### 4️⃣ Run the System

```bash
python3 main.py
```

---

## ✅ Sample Output

```json
{
  "final_decision": "BLOCK",
  "confidence": 97,
  "action": "Remove review and flag account for investigation"
}
```

---

## 🧠 How It Works

1. Input is loaded from `input.txt`
2. Three agents run **in parallel**:

   * Reviewer Credibility Agent
   * Content Authenticity Agent
   * Purchase Verification Agent
3. A Final Decision Agent aggregates results using deterministic rules
4. The system outputs an explainable moderation decision

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **LangGraph** (agent orchestration)
* **Google Gemini**

---

## 📌 Notes

* This project uses **prompt-based reasoning only**
* All signals are assumed or provided via input
* Designed for **real-time moderation systems**


## 👩‍💻 Author

Built as a **research-style multi-agent system** to demonstrate explainable AI moderation using modern agent orchestration frameworks.
