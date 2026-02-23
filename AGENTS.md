# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

GenAI4Humanists is an educational repository for a course on "Generative AI for Humanists". It contains Jupyter notebooks demonstrating various GenAI concepts, from basic OpenAI/Azure interactions to advanced RAG systems, agents, and fine-tuning open-source models.

## Repository Structure

- `lessons/`: Course materials organized by topic (Intro, LlamaIndex, LangChain, LlamaAgents, OpenSource)
- `src/`: Helper utilities for notebooks (API client setup, visualization tools, MultiOn integration)
- `Data/`: Datasets in multiple formats (txt, pdf, csv, html, mp3, images, JSON)
- `Index/`: LlamaIndex-generated search indices (VectorStoreIndex, TreeIndex, KeywordIndex, etc.)
- `.env`: API keys (OPENAI_API_KEY, GEMINI_API_KEY, MULTION_API_KEY) - not committed to git

## Environment Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Lab to work with notebooks
jupyter lab
```

## Key Dependencies

- **LLM APIs**: `openai`, `google-genai`, `ollama`
- **Frameworks**: `llama-index`, `langchain`, `crewai`
- **ML/NLP**: `transformers`, `sentence-transformers`, `torch`, `bitsandbytes`, `peft`
- **UI/Visualization**: `gradio`, `streamlit`, `matplotlib`, `PIL`
- **Data Processing**: `pandas`, `beautifulsoup4`, `pdf2image`
- **Utilities**: `python-dotenv`, `nest-asyncio`, `websockets`

## Architecture Patterns

### Helper Module Pattern
The `src/` directory provides reusable utilities:

- `src/helper.py`: Core OpenAI/MultiOn client setup and API key management
  - `load_env()`: Loads environment variables from `.env`
  - `get_openai_client()`: Returns configured OpenAI client
  - `get_multi_on_client()`: Returns MultiOn browser automation client
  - `visualizeCourses()`: Renders scraped course data as HTML tables in notebooks

- `src/utils.py`: Advanced MultiOn browser automation utilities
  - `SessionManager`: Manages persistent browser sessions, navigation, task execution
  - `MultiOnDemo`: Full Gradio-based browser automation demo with chat interface
  - `ImageUtils`: Screenshot downloading and processing
  - `visualizeSession()`: Displays MultiOn session responses with formatted HTML
  - `display_step_header()`: Creates visual step separators in notebooks

### Notebook Import Pattern
Most notebooks use relative imports from `src/`:
```python
import sys
sys.path.append('../../src')  # Adjust depth based on lesson location
from helper import get_openai_client, load_env
```

### LlamaIndex Patterns
- **Index Storage**: Indices are persisted to `Index/` directory for reuse across notebooks
- **Common Index Types**: VectorStoreIndex (semantic search), TreeIndex (hierarchical), KeywordIndex (keyword-based)
- **Agent Architecture**: Notebooks use LlamaIndex's agent reasoning loops (ReAct, function calling, stepwise control)

### Data Loading Patterns
- Text files are loaded from `Data/txt/`
- PDFs from `Data/pdf/`
- CSVs from `Data/csv/`
- Images from `Data/imgs/` or `Data/RAG_images/`
- Notebooks expect data in these specific subdirectories

### Environment Variable Usage
Notebooks load API keys via:
```python
from dotenv import load_dotenv
load_dotenv("../../.env", override=True)  # Path relative to notebook location
```

## Lesson Categories

1. **Intro**: Basic LLM interactions, prompt engineering, multimodal models, hallucinations
2. **LlamaIndex**: RAG implementations, chatbots, agents, evaluation, Streamlit integration
3. **LangChain**: Chains, semantic search, RAG patterns
4. **LlamaAgents**: Advanced agent architectures (router engines, tool calling, multi-document agents, ReAct)
5. **OpenSource**: Local model deployment (Ollama, Qwen 2.5, Llama 3.2, Ministral), fine-tuning

## Working with Notebooks

- All notebooks are `.ipynb` files meant to be run in Jupyter Lab
- Checkpoints are stored in `.ipynb_checkpoints/` (ignored by git)
- Many notebooks have companion `.py` files (exports or Streamlit apps)
- Notebooks often demonstrate progressive complexity within a topic

## MultiOn Browser Automation

Several notebooks use MultiOn for web automation:
- `SessionManager` creates and manages browser sessions
- Sessions execute tasks via natural language commands
- Screenshots and responses are captured and visualized
- `MultiOnDemo` provides a Gradio UI wrapper for interactive exploration

## Fine-Tuning Patterns

Fine-tuning notebooks (in `OpenSource/Fine-tune/`) demonstrate:
- Loading models with `transformers` and `bitsandbytes` for quantization
- Using PEFT/LoRA for parameter-efficient fine-tuning
- Training with `trl` (Transformers Reinforcement Learning)
- Model evaluation and comparison

## Important Notes

- This is a teaching repository, not production code
- Notebooks are designed for educational exploration and may contain experimental code
- The `.venv/` directory contains the virtual environment (not tracked in git)
- Index files in `Index/` are pre-built to save computation time across lessons
