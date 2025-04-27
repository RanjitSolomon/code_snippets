# Local Deep Researcher
          
$> git clone git@github.com:langchain-ai/local-deep-researcher.git

$> cp .env-example .env

$> cd local-deep-researcher
$> uv sync 
$> uv pip install -U "langgraph-cli[inmem]"
$> uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev

Settings - Assistant - create a new assistant 
Assistant Name: gemma3assistant
Research Depth - 3
LLM Model Name: gemma3
LLM Provider: ollama
Search API: duckduckgo
check - ollama Base URL: http://localhost:11434

"Give me an overview of Model Context Protocol and usage with cursor as an example"

add .env file
LLM_PROVIDER=ollama
LOCAL_LLM=gemma3

Comment out
# Web Search API Keys (choose one or both)
# TAVILY_API_KEY=tvly-xxxxx      # Get your key at https://tavily.com
# PERPLEXITY_API_KEY=pplx-xxxxx  # Get your key at https://www.perplexity.ai

#-------- .env --------------------------
# Which search service to use, either 'duckduckgo', 'tavily', 'perplexity', Searxng
SEARCH_API='duckduckgo'
# For Searxng search, defaults to http://localhost:8888
SEARXNG_URL=

# Web Search API Keys (choose one or both)
# TAVILY_API_KEY=tvly-xxxxx      # Get your key at https://tavily.com
# PERPLEXITY_API_KEY=pplx-xxxxx  # Get your key at https://www.perplexity.ai

# LLM Configuration
LLM_PROVIDER=ollama #lmstudio          # Options: ollama, lmstudio
LOCAL_LLM=gemma3  #qwen_qwq-32b         # Model name in LMStudio/Ollama
# LMSTUDIO_BASE_URL=http://localhost:1234/v1  # LMStudio OpenAI-compatible API URL
OLLAMA_BASE_URL=http://localhost:11434 # the endpoint of the Ollama service, defaults to http://localhost:11434 if not set

MAX_WEB_RESEARCH_LOOPS=3
FETCH_FULL_PAGE=True

LANGCHAIN_API_KEY="lsvxxxxxxxxxxxxxxxxxxxxxxxxxxxxa8"
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="ollama-langchain"

#==========================================

