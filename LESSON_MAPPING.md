# Lesson-to-Module Mapping

## Quick Reference: Which notebook covers which topic?

---

## Module 1: Foundations of Generative Architectures

| Topic | Status | Notebook | Notes |
|-------|--------|----------|-------|
| Neural Network Fundamentals | 🟡 External | [NeuralNetworks_Course/Notebooks/Numpy/04a_Numpy_NeuralNetworks.ipynb](https://github.com/rsouza/NeuralNetworks_Course/blob/main/Notebooks/Numpy/04a_Numpy_NeuralNetworks.ipynb) | |
| Transformers & Attention | 🟡 External | [NeuralNetworks_Course/Notebooks/PyTorch/Attention/PT_the-annotated-transformer.ipynb](https://github.com/rsouza/NeuralNetworks_Course/blob/main/Notebooks/PyTorch/Attention/PT_the-annotated-transformer.ipynb) | |
| Latent Space Concepts | 🟡 External | [NeuralNetworks_Course/Notebooks/PyTorch/AE/](https://github.com/rsouza/NeuralNetworks_Course/tree/main/Notebooks/PyTorch/AE) | Autoencoders folder |
| Comparative: Text (LLMs) | 🟡 Partial | `Intro/OpenAI_Intro.ipynb` | API focus, needs theory |
| Comparative: Images (Diffusion) | 🟢 Available | `Intro/MultiModal_Models.ipynb` | |
| Comparative: Speech (TTS/STT) | 🟢 Available | `Intro/MultiModal_Models.ipynb` | Whisper, TTS |

---

## Module 2: The Art of Interaction & Integration

| Topic | Status | Notebook | Notes |
|-------|--------|----------|-------|
| Zero-shot Prompting | 🟢 Available | `Intro/Prompt_Guidelines.ipynb` | |
| Few-shot Prompting | 🟢 Available | `Intro/Advanced_Prompting.ipynb` | |
| Chain-of-Thought | 🟢 Available | `Intro/Advanced_Prompting.ipynb` | |
| OpenAI API | 🟢 Available | `Intro/OpenAI_Intro.ipynb` | |
| Azure OpenAI | 🟢 Available | `Intro/Azure_Intro.ipynb` | |
| Google Gemini | 🟢 Available | `Intro/Gemini_Intro.ipynb` | |
| Anthropic Claude | 🟢 Available | `Intro/Anthropic_Intro.ipynb` | |
| Hugging Face | 🟢 Available | `OpenSource/Qwen_2.5/`, `OpenSource/Llama_3.2/`, `OpenSource/Fine-tune/` | Extensive coverage |
| Ollama | 🟡 Partial | `OpenSource/Use_Cases/` | 2 notebooks |

---

## Module 3: Frameworks & Orchestration

| Topic | Status | Notebook | Notes |
|-------|--------|----------|-------|
| LangChain Basics | 🟢 Available | `LangChain/Intro_Lanchain_Chains.ipynb` | |
| LangChain Chains | 🟢 Available | `LangChain/Intro_Lanchain_Chains.ipynb` | |
| LlamaIndex Basics | 🟢 Available | `LlamaIndex/` | Multiple notebooks |
| RAG Implementation | 🟢 Available | `LlamaIndex/`, `Agentic_RAG_From_Scratch.ipynb` | |
| Vector Databases | 🟢 Available | `Index/` | Pre-built indices |
| Fine-tuning | 🟡 Partial | `OpenSource/Fine-tune/` | |
| In-Context Learning | 🟢 Available | `Intro/Few-shot examples` | |

---

## Module 4: Autonomous Agents & The Future of Work

| Topic | Status | Notebook | Notes |
|-------|--------|----------|-------|
| Agentic AI Pipelines | 🟡 Partial | `Agentic_RAG_From_Scratch.ipynb` | |
| LlamaIndex Agents | 🟡 Partial | `LlamaIndex/` | |
| Tool Calling | 🔴 Missing | - | Needs creation |
| Large Action Models | 🔴 Missing | - | Needs creation |
| Claude Code CLI | 🔴 Missing | - | Needs creation |
| Gemini CLI | 🔴 Missing | - | Needs creation |
| Bias in LLMs | 🟡 Partial | `Intro/Hallucinations.ipynb` | Related topic |
| Deepfake Forensics | 🔴 Missing | - | Needs creation |
| Responsible AI | 🔴 Missing | - | Needs creation |

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 🟢 Available | Complete, ready to use in this repo |
| 🟡 External | Available in external repo (NeuralNetworks_Course) - click link to access |
| 🟡 Partial | Available but needs improvement |
| 🔴 Missing | Not yet created |

---

## Priority Actions

### High Priority (must have for course)
1. Create `lessons/Ethics/Responsible_AI.ipynb` - Bias, fairness, deployment
2. Create `lessons/Ethics/Deepfake_Forensics.ipynb` - Detection techniques

### Medium Priority (important)
3. Expand Ollama section with more examples
4. Add Agentic CLI tutorials (Claude Code, Gemini CLI)
5. Add Tool Calling notebook

### Lower Priority (nice to have)
6. Create Latent Space visualization notebook (reference NeuralNetworks_Course AE folder)
