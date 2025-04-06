import os


os.environ["OPENAI_BASE_URL"] = 'http://localhost:11434/v1'
os.environ["OPENAI_API_KEY"] = 'fake-key'

from praisonaiagents import Agent
from glob import glob
 
config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "praison",
            "path": ".praison"
        }
    },
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "deepseek-coder-v2",
            "ollama_base_url": "http://localhost:11434",
        },
    },
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest",
            "ollama_base_url": "http://localhost:11434",
            "embedding_dims": 1536
        },
    },
}


knowledge = [path for path in glob('..\move-book\\**\\*.md')]

agent = Agent(
    name="Knowledge Agent",
    instructions="You answer questions based on the provided knowledge.",
    knowledge=knowledge,
    knowledge_config=config,
    user_id="user1",
    llm="deepseek-coder-v2"
)

agent.start("What is SUI in one line?") # Querying