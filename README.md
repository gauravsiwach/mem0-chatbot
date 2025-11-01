# Memory-Aware Chat Assistant

This is a chat app where we are building memory of the user or chat with Mem0, that extracts the memory from user chats and saves it.

This project implements a memory-aware chat assistant using the Mem0 library. It integrates OpenAI's GPT model for generating responses and Qdrant as a vector store for managing user memories.

## Features

- **Memory Management**: Stores and retrieves user interaction memories to provide context-aware responses.
- **AI-Powered Responses**: Uses OpenAI's GPT-4o-mini model to generate replies based on user input and past memories.
- **Vector Storage**: Employs Qdrant for efficient memory search and storage.

## Setup

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Configure environment variables in `.env`:
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `QDRANT_API_KEY`: Your Qdrant API key.

3. Run the chat assistant:
   ```sh
   python main.py
   ```

## Usage

- Start the chat by running the script.
- Type your messages; the assistant will respond with context from past interactions.
- Press Ctrl+C to quit.

## Dependencies

- `openai`: For AI model interactions.
- `python-dotenv`: For loading environment variables.
- `mem0`: For memory management.