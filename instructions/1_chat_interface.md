## Customer Support Chat Interface

Here you can find the instructions to run the Customer Support chat interface we want to test today.

### Installation

1. Create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Or on Windows
.venv\Scripts\activate
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file following the template below:

```bash
# Template file
API_URL=<ENDPOINT>
CUSTOMER_EMAIL=john.doe@example.com
```

We will share the endpoint URL in our presentation.

### Usage

Run the Streamlit app:

```bash
streamlit run customer_support_chat.py
```

The app will open in your default browser at `http://localhost:8501`

### How It Works

- Each conversation is assigned a unique session ID to maintain context
- The app maintains chat history during the session
- Use the "Start New Conversation" button in the sidebar to reset and begin a fresh conversation

## Manual Prompt Injection
Some material on how to build adversarial prompts:
- https://learnprompting.org/docs/prompt_hacking/injection
- https://fdzdev.medium.com/20-prompt-injection-techniques-every-red-teamer-should-test-b22359bfd57d
- https://promptintel.novahunting.ai/feed