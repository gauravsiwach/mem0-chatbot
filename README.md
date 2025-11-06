# Mem0 Chatbot with Neo4j Integration

A memory-aware chat assistant that uses Mem0 for intelligent memory management, combining vector storage (Qdrant) and graph storage (Neo4j) to provide context-aware conversations.

## Features

- **Intelligent Memory Management**: Uses Mem0 to extract, store, and retrieve user memories from conversations
- **Dual Storage Architecture**:
  - **Vector Store**: Qdrant for semantic search and similarity matching
  - **Graph Store**: Neo4j for relationship-based memory connections (optional)
- **AI-Powered Responses**: OpenAI GPT-4o-mini for generating contextual replies
- **Persistent Memory**: Maintains conversation history and user preferences across sessions
- **Flexible Configuration**: Choose between basic vector-only or advanced graph+vector memory

## Project Structure

- `main.py` - Basic chat assistant with Qdrant vector storage only
- `memory-with-neo4j.py` - Advanced chat assistant with both Qdrant and Neo4j integration
- `requirements.txt` - Python dependencies
- `.env` - Environment variables configuration

## Setup

### Prerequisites

- Python 3.8+
- OpenAI API key
- Qdrant account (for vector storage)
- Neo4j Aura account (for graph storage, optional)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gauravsiwach/mem0-chatbot.git
   cd mem0-chatbot
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   QDRANT_API_KEY=your_qdrant_api_key_here
   NEO4J_URL=your_neo4j_connection_url
   NEO4J_USERNAME=your_neo4j_username
   NEO4J_PASSWORD=your_neo4j_password
   ```

## Usage

### Basic Version (Qdrant only)

Run the basic chat assistant with vector storage:
```bash
python main.py
```

### Advanced Version (Qdrant + Neo4j)

Run the advanced chat assistant with graph and vector storage:
```bash
python memory-with-neo4j.py
```

### How it works

1. **Memory Extraction**: Mem0 analyzes user messages to extract key memories and relationships
2. **Context Retrieval**: Searches existing memories to provide relevant context
3. **Response Generation**: OpenAI GPT generates responses using conversation history and retrieved memories
4. **Memory Storage**: Saves new memories to both vector store (Qdrant) and graph store (Neo4j, if enabled)

## Configuration

The chat assistant can be configured through the `config` dictionary in each script:

- **Embedder**: OpenAI text-embedding-3-small for creating vector representations
- **LLM**: OpenAI GPT-4o-mini for response generation
- **Vector Store**: Qdrant cloud instance for semantic search
- **Graph Store**: Neo4j Aura database for relationship storage (optional)

## Dependencies

Key packages:
- `mem0ai` - Memory management and extraction
- `openai` - AI model integration
- `qdrant-client` - Vector database client
- `neo4j` - Graph database driver
- `langchain` - Framework for LLM applications
- `python-dotenv` - Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the Mem0 documentation: https://docs.mem0.ai/
- Neo4j Aura: https://neo4j.com/cloud/aura/
- Qdrant Cloud: https://qdrant.tech/