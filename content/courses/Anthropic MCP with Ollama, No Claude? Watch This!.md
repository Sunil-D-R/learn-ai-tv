---
categories:
- Development
date: 2024-10-27
description: Learn how to build a native Model Context Protocol application that connects
  to LLMs hosted on various platforms like Llama and OpenAI.
duration: 29 minutes
layout: course
level: Intermediate
sections:
- description: Overview of Model Context Protocol and its limitations, focusing on
    the need for broader LLM compatibility and native application integration.
  timestamp: 00:00
  title: "\U0001F3A5 Introduction: Extending Model Context Protocol"
- description: A practical demonstration showcasing the custom CLI application, connecting
    to OpenAI's GPT-4 mini and Llama 3.2, querying a SQL database using function calling.
  timestamp: 01:09
  title: "\U0001F680 CLI Demo:  Connecting to OpenAI and Llama"
- description: Explanation of the application architecture, including the host, clients,
    and servers. A detailed look at the server-side setup using standard IO and UVX.
  timestamp: 04:29
  title: ⚙️ Architecture and Server Setup
- description: Breakdown of the Model Context Protocol's communication mechanism,
    emphasizing the JSON-RPC messages, initialization, capabilities exchange, and
    notification messages.
  timestamp: 06:59
  title: "\U0001F9F1 Protocol Deep Dive: Messages and Initialization"
- description: 'Presentation of a stripped-down version of the code in test.py, highlighting
    the core logic for initialization, pinging, and handling messages. '
  timestamp: '12:46'
  title: "\U0001F6E0️ Simplified Implementation: test.py"
- description: Detailed explanation of the chat mode functionality, demonstrating
    how tools are fetched, system prompts generated, and function calling integrated
    with OpenAI and Llama.
  timestamp: '19:48'
  title: "\U0001F5E3️ Chat Mode Implementation: Function Calling"
- description: Step-by-step walkthrough of handling tool calls received from the LLM,
    parsing messages, sending calls via sendCallTool, and updating conversation history.
  timestamp: '24:24'
  title: "\U0001F9F0 Handling Tool Calls and the Conversation History"
- description: Summary of the process, encouraging viewers to build their own applications
    using the provided examples and expand the Model Context Protocol ecosystem.
  timestamp: '29:19'
  title: "\U0001F3AF Conclusion: Building and Expanding the Ecosystem"
tags:
- Model Context Protocol
- Anthropic
- OpenAI
- Llama
- Function Calling
- JSON-RPC
- CLI
thumbnail: https://i.ytimg.com/vi/9mciRwpcLNY/sddefault.jpg
title: Building Your Own Native Model Context Protocol Application
videoId: 9mciRwpcLNY
---