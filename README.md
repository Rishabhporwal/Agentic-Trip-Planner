# Agentic-Trip-Planner 🧳✈️

An **LLM-powered intelligent travel planner** that generates personalized trip itineraries using real-time data — including weather, places of interest, currency conversion, and expense estimation. Built with **LangGraph**, **FastAPI**, **Streamlit**, and integrates with **Groq** or **OpenAI**.

---

## ✨ Features

- 🔗 **Agentic architecture** using LangGraph
- 🔧 Tool-augmented LLMs: Weather, Place Search, Expense Calculator, Currency Converter
- 💬 Simple user interface via Streamlit
- 🚀 Backend powered by FastAPI
- 🌍 Real-time data: Weather, location info, exchange rates
- 📄 Outputs structured **Markdown itineraries**
- 🔁 Supports Groq and OpenAI as LLM providers

---


## 🚀 Quickstart

### 1. Clone and set up environment

```bash
git clone https://github.com/Rishabhporwal/Agentic-Trip-Planner.git
cd Agentic-Trip-Planner
python -m venv .venv
uv source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
uv pip install --upgrade pip
uv pip install -r requirements.txt
```

### 3. Configure API Keys

```bash
| Variable                | Description                             |
| ----------------------- | --------------------------------------- |
| `GROQ_API_KEY`          | Groq (for fast LLaMA3 inference)        |
| `OPENAI_API_KEY`        | OpenAI fallback                         |
| `OPENWEATHER_API_KEY`   | OpenWeatherMap for real-time weather    |
| `GPLACES_API_KEY`       | Google Places for tourist attractions   |
| `EXCHANGE_RATE_API_KEY` | Currency rates via exchangerate-api.com |
| `TAVILY_API_KEY`        | (Optional) Tavily for fallback search   |
| `LANGCHAIN_API_KEY`     | (Optional) for LangSmith traces         |

```
### 4. Run the API Backend

```bash
uvicorn main:app --reload
```


### 5. Run the Streamlit App (Frontend)

```bash
streamlit run streamlit_app.py
```


