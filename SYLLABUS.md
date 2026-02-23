# GenAI for Humanists - Course Syllabus

**Course Code:** 136031  
**Semester:** 2026S  
**Institution:** Universität Wien  
**Type:** UE (Exercise Course)  
**ECTS:** To be confirmed

---

## Course Description

This course provides a comprehensive introduction to Generative AI for humanities students and researchers. No prior programming experience is required, though basic Python knowledge is beneficial. The course emphasizes hands-on practical skills combined with critical theoretical understanding of AI technologies relevant to humanities research.

---

## Aims, Contents and Method

### Module 1: Foundations of Generative Architectures
**Focus:** How the "brain" works before we talk to it.

- Neural Network Fundamentals: Understanding Transformers, Attention Mechanisms, and Latent Space
- Comparative analysis of models for Text (LLMs), Images (Diffusion), and Speech (TTS/STT)

### Module 2: The Art of Interaction & Integration
**Focus:** Moving from basic prompts to programmatic control.

- Advanced Prompt Engineering: Master Zero-shot, Few-shot, and Chain-of-Thought (CoT) prompting
- The API Ecosystem: Hands-on integration with proprietary leaders (OpenAI, Google Gemini)
- The Open Source Ecosystem: Using Hugging Face and Ollama

### Module 3: Frameworks & Orchestration
**Focus:** Connecting LLMs to external data and tools.

- Python LLM Frameworks: In-depth development using LangChain and LlamaIndex
- RAG (Retrieval-Augmented Generation): Connecting models to private data sources
- Model Optimization: The technical trade-offs of Fine-Tuning vs. In-Context Learning

### Module 4: Autonomous Agents & The Future of Work
**Focus:** Developing AI that "acts" rather than just "speaks."

- Agentic AI Pipelines: Building loops where AI can self-correct and use external tools
- Large Action Models (LAMs): Understanding the shift from generating text to executing tasks
- The Terminal as an Interface: Mastering Agentic CLIs (like Claude Code or Gemini CLI) for rapid development
- Ethics & Governance: Tackling bias, deepfake forensics, and the "Responsible AI" deployment cycle

---

## Course Content Summary

- Social, Technical and Practical aspects of GenAI
- LLMs and other Generative Models
- LLMs and GenAI for Humanities
- Prompt Engineering Techniques
- Python Frameworks
- Few-shots learning
- Fine Tuning models
- Using APIs
- Working with Images
- Working with speech data
- Working with tabular data
- Large Action Models - Agents

---

## Assessment and Grading

**Evaluation Method:** Continuous assessment through hands-on assignments

- **Individual Assignments:** Regular practical exercises (60%)
- **Group Projects:** Collaborative work on applied problems (20%)
- **Final Capstone Project:** Comprehensive applied project (20%)
- **Participation:** Class discussion and activities

**Requirements:**
- Attendance is required
- Regular participation is essential
- All students must provide their own computing environment
- Homework assignments must be submitted on time
- Final project must be submitted on time

**Note:** There is no final examination for this course.

---

## Weekly Schedule

| Week | Topic | Module | Notebooks | Status |
|------|-------|--------|-----------|--------|
| 1 | Introduction to AI for Humanities | 1 | Course intro, setup | 🟢 |
| 2 | How LLMs Work: Transformers & Attention | 1 | NeuralNetworks_Course (external) | 🟡 External |
| 3 | Comparative Models: Text, Image, Audio | 1 | `Intro/MultiModal_Models.ipynb` | 🟢 |
| 4 | Basic Prompting & API Access | 2 | `Intro/OpenAI_Intro.ipynb`, `Intro/Azure_Intro.ipynb` | 🟢 |
| 5 | Advanced Prompt Engineering | 2 | `Intro/Prompt_Guidelines.ipynb`, `Intro/Advanced_Prompting.ipynb` | 🟢 |
| 6 | Open Source Models: Hugging Face & Ollama | 2 | `OpenSource/` notebooks | 🟡 Partial |
| 7 | Introduction to LangChain | 3 | `LangChain/Intro_Lanchain_Chains.ipynb` | 🟢 |
| 8 | Introduction to LlamaIndex | 3 | `LlamaIndex/` notebooks | 🟢 |
| 9 | RAG Systems: Building Knowledge Assistants | 3 | `LlamaIndex/`, `Agentic_RAG_From_Scratch.ipynb` | 🟢 |
| 10 | Fine-tuning vs In-Context Learning | 3 | `OpenSource/Fine-tune/` notebooks | 🟡 Partial |
| 11 | Autonomous Agents: Theory & Practice | 4 | `LlamaAgents/`, `Agentic_RAG_From_Scratch.ipynb` | 🟡 Partial |
| 12 | Agentic CLIs: Claude Code, Gemini CLI | 4 | *To be added* | 🔴 |
| 13 | Ethics: Bias, Deepfakes, Responsible AI | 4 | *To be added* | 🔴 |
| 14 | Final Project Presentations | 4 | Capstone | 🟢 |
| 15 | Course Reflection & Future Directions | 4 | Discussion | 🟢 |

**Legend:** 🟢 Available | 🟡 Partial/External | 🔴 Missing

---

## Recommended Background Reading

Reading and video lists will be published on Moodle.

### External Prerequisites

For Module 1 (Foundations), students should reference the **NeuralNetworks_Course** repository for foundational theory:

**GitHub:** https://github.com/rsouza/NeuralNetworks_Course

**Recommended Notebooks:**

| Topic | Location | File | Link |
|-------|----------|------|------|
| Neural Network Basics | `Notebooks/Numpy/` | `04a_Numpy_NeuralNetworks.ipynb` | [Link](https://github.com/rsouza/NeuralNetworks_Course/blob/main/Notebooks/Numpy/04a_Numpy_NeuralNetworks.ipynb) |
| Activation Functions | `Notebooks/Numpy/` | `07_Numpy_ActivationsFunctions.ipynb` | [Link](https://github.com/rsouza/NeuralNetworks_Course/blob/main/Notebooks/Numpy/07_Numpy_ActivationsFunctions.ipynb) |
| Transformer Architecture | `Notebooks/PyTorch/Attention/` | `PT_the-annotated-transformer.ipynb` | [Link](https://github.com/rsouza/NeuralNetworks_Course/blob/main/Notebooks/PyTorch/Attention/PT_the-annotated-transformer.ipynb) |
| Transformer from Scratch | `Notebooks/PyTorch/Attention/` | `PT_transformer_from_scratch.ipynb` | [Link](https://github.com/rsouza/NeuralNetworks_Course/blob/main/Notebooks/PyTorch/Attention/PT_transformer_from_scratch.ipynb) |
| Annotated Transformer | `Notebooks/PyTorch/Transformers/` | `PT_Annotated_Transformer.ipynb` | [Link](https://github.com/rsouza/NeuralNetworks_Course/blob/main/Notebooks/PyTorch/Transformers/PT_Annotated_Transformer.ipynb) |
| Latent Space (Autoencoders) | `Notebooks/PyTorch/AE/` | Multiple notebooks | [Link](https://github.com/rsouza/NeuralNetworks_Course/tree/main/Notebooks/PyTorch/AE) |

These notebooks provide the theoretical background on neural networks, attention mechanisms, Transformers, and latent space concepts needed before working with LLMs.

### Additional Reading
- Transformers architecture documentation
- LangChain/LlamaIndex documentation
- Ethics in AI (to be provided)

---

## Repository Structure

```
GenAI4Humanists/
├── lessons/           # Course notebooks organized by topic
│   ├── Intro/        # Basic LLM interactions, prompting, multimodal
│   ├── LangChain/    # LangChain framework tutorials
│   ├── LlamaIndex/   # LlamaIndex and RAG implementations
│   ├── LlamaAgents/  # Agent architectures
│   └── OpenSource/   # Local models, fine-tuning
├── src/              # Helper utilities
├── Data/             # Datasets for exercises
├── Index/            # Pre-built LlamaIndex indices
├── AGENTS.md         # AI assistant guidance
├── SYLLABUS.md       # This file
├── LESSON_MAPPING.md # Topic-to-notebook mapping
└── requirements.txt  # Python dependencies
```

---

## Technical Requirements

- Python 3.10+
- Jupyter Lab
- API keys: OpenAI, Google Gemini (provided or personal)
- GitHub account (for assignments)

---

## Instructor

[To be completed]

**Office Hours:** [To be announced]

**Contact:** [To be completed]
