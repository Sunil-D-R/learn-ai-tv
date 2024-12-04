---
title: "Build an AI Chatbot with N8N and Google Drive"
date: 2024-10-27
layout: course
description: "Learn how to build an AI-powered chatbot that answers questions using documents from your Google Drive, integrated with a website using N8N."
categories: ["Automation", "Prompt Engineering"]
duration: "22 minutes"
level: "Intermediate"
tags: ["N8N", "AI Agent", "Google Drive", "Pinecone", "OpenAI", "Chatbot", "RAG", "Embedding", "Vector Database", "Workflow Automation"]
thumbnail: "https://i.ytimg.com/vi/UeFi5oV9UpY/sddefault.jpg"
videoId: "UeFi5oV9UpY"
sections:
  - title: "🎥 Introduction: Building an Intelligent Chatbot"
    description: "Overview of building a RAG chatbot using N8N's AI Agent node, capable of answering questions from various data sources. Introduction of the project: a chatbot answering questions from a Google Drive knowledge base."
    timestamp: "00:00"
  - title: "🚀 Project Overview & Setup: Two-Phase Approach"
    description: "Detailed explanation of the two phases: data loading into a vector store (Pinecone) and building the AI assistant.  Initial setup steps and workflow overview."
    timestamp: "01:59"
  - title: "⚙️ Phase 1: Loading Data into Pinecone"
    description: "Step-by-step guide to setting up a Google Drive trigger in N8N to automatically upload data to Pinecone when files are added to a specific folder. Includes Google Cloud Platform setup, API key generation, and workflow testing."
    timestamp: "02:38"
  - title: "📌 Connecting Google Drive & Pinecone: API Keys & Workflow"
    description: "Connecting Google Drive and Pinecone using N8N nodes.  Setting up credentials, configuring triggers for file uploads, downloading files, and integrating with Pinecone for vector database storage. Detailed explanation of the process."
    timestamp: "08:41"
  - title: "🤖 Phase 2: Building the AI Assistant"
    description: "Creating the AI assistant workflow in N8N using the AI Agent node.  Setting up the chat interface, configuring the AI Agent (Tool Agent), system messages, and memory."
    timestamp: "12:57"
  - title: "🔗 Connecting OpenAI and Customizing the Agent"
    description: "Integrating OpenAI for both embedding and the chat model. Setting up the OpenAI API key, selecting the GPT-4-0 Mini model, and configuring the memory node for context preservation."
    timestamp: "15:13"
  - title: "🌐 Sharing and Embedding: Public URL & Website Integration"
    description: "Explains how to share the chatbot with a public URL and embed it into a website.  Details on enabling public access in N8N, password protection, and generating embedding code for website integration."
    timestamp: "17:54"
  - title: "🎨 Customization: Styling the Chatbot"
    description: "A detailed walkthrough of customizing the chatbot's appearance, including initial messages, color schemes, and layout. Uses CSS variables and shows how to integrate custom styles with the embedded chatbot."
    timestamp: "19:56"

---