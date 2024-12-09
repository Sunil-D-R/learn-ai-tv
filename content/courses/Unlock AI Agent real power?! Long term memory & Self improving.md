---
title: "Building AI Agents with Long-Term Memory"
date: 2024-10-27
layout: course
description: "Explore techniques for building AI agents capable of learning from past interactions and retaining user preferences using long-term memory."
categories: ["Agent Development", "Prompt Engineering", "Memory Management"]
duration: "22 minutes"
level: "Intermediate"
tags: ["AI Agents", "Long-Term Memory", "AutoGen", "Large Language Models", "Vector Databases", "Chroma"]
thumbnail: "https://i.ytimg.com/vi/7LWTZqksmSg/sddefault.jpg"
videoId: "7LWTZqksmSg"
sections:
  - title: "🤔 The Need for Long-Term Memory in AI Agents"
    description: "Discussion on the limitations of dataless AI agents and the benefits of incorporating memory for improved user experience and task efficiency."
    timestamp: "00:00"
  - title: "🧠 How Humans Learn: A Guiding Principle"
    description: "Analogy of human learning process (attention, encoding, consolidation, long-term memory) to illustrate the concept of long-term memory in AI agents.  Discusses the difference between how human memories can fade and how AI agents can maintain perfect memory."
    timestamp: "02:16"
  - title: "🤖 Architecting a Knowledge Agent"
    description: "Explanation of a knowledge agent architecture which processes user-agent interactions to identify and store valuable information in a vector database for later retrieval.  Illustrative example of storing user preferences (e.g., dietary restrictions)."
    timestamp: "03:11"
  - title: "🚀 Optimizing Knowledge Retrieval"
    description: "Strategies for optimizing knowledge retrieval to balance speed, accuracy and cost. This includes using cheaper models for initial checks, prioritization of information, and archiving older, less-frequently used data."
    timestamp: "04:49"
  - title: "💡 Real-world Examples and Implementations"
    description: "Examples of projects implementing long-term memory in AI agents: MIM GPT (Memory GPT),  continuously learning language agent (CLNA), and enhanced customer support agents.  These examples highlight different approaches and applications."
    timestamp: "05:41"
  - title: "🛠️ Implementing Long-Term Memory in AutoGen (Practical Example)"
    description: "Step-by-step tutorial on adding long-term memory to an AutoGen agent in under 10 minutes. This covers setting up configurations, installing necessary packages, and using the `teachable` agent ability."
    timestamp: "13:14"
  - title: "🔎 Deep Dive into AutoGen's Teachable Agent"
    description: "Detailed explanation of the `teachable` agent's components, including the `MemoStore` class for database interaction, the `TextAnalyzer` agent, and the `storage` and `retrieval` functions."
    timestamp: "17:58"

---