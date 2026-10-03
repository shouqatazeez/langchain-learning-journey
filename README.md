# LangChain Learning Journey

A hands-on repository documenting my journey learning LangChain for building LLM-powered applications. I'm learning in public and committing as I go, so this repo grows with every new topic I work through.

One thing worth noting: I studied how the major closed-source models work (OpenAI, Claude, Gemini), but I run the projects here on open-source models through Hugging Face to keep everything cost-free. The LangChain code barely changes between them, which turned out to be one of the most useful lessons here.

## The 6 Core Components

LangChain is built around six components. Rather than treating it as a hundred separate features, I've found it much easier to think of it as these building blocks. Here's where I am:

| # | Component | Status | What it does |
|---|-----------|--------|--------------|
| 1 | Models | Done | A standard interface to talk to any LLM — covers both chat and embedding models |
| 2 | Prompts | Done | Dynamic, reusable, role-based instructions for the model |
| 3 | Chains | Done | Piping components together, e.g. `prompt \| model` |
| 4 | Memory | Done | Giving a conversation state so the model remembers earlier turns |
| 5 | Indexes | Upcoming | Connecting the LLM to external data (RAG) |
| 6 | Agents | Upcoming | Models that reason and use tools to take actions |

Next on my list: Structured Outputs — getting the model to return clean, predictable data like JSON instead of free-form text.

## What's Inside

### ChatModels/

| File | Topic |
|------|-------|
| `1_chatmodel_hf_api.py` | Calling a chat model through the Hugging Face API |
| `messages.py` | Message types — `SystemMessage`, `HumanMessage`, `AIMessage` |
| `chatbot.py` | A chatbot that remembers conversation history |
| `chat_prmpt_template.py` | Role-based prompts with `ChatPromptTemplate` |
| `embedding_hf_local.py` | Embedding models — turning text into vectors |

### Prompts/

| File | Topic |
|------|-------|
| `static.py` | A static prompt wired into a simple Streamlit UI |
| `dynamic.py` | A dynamic prompt using `PromptTemplate` placeholders |
| `prompt_generator.py` | Building a prompt and saving it to JSON |
| `template.json` | The saved prompt template |
| `dynamic2.py` | Loading a saved prompt and running it as a chain |

### Root

| File | Purpose |
|------|---------|
| `requirements.txt` | Project dependencies |
| `test.py` | A quick LangChain version check |

## Getting Started

Clone the repo and set up a virtual environment:

```bash
git clone <your-repo-url>
cd Langchain
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS / Linux
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Add your API keys in a `.env` file at the project root. This file is git-ignored, so it stays private:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Then run any example:

```bash
# A plain script
python ChatModels/1_chatmodel_hf_api.py

# A Streamlit app
streamlit run Prompts/dynamic2.py
```

## Tech Stack

- LangChain (`langchain`, `langchain-core`, `langchain-huggingface`)
- Hugging Face models — `Qwen/Qwen2.5-3B-Instruct` and `all-MiniLM-L6-v2`
- Streamlit for the UIs
- python-dotenv for managing environment variables

---

If you're learning GenAI too, feel free to follow along as this repo grows topic by topic.
