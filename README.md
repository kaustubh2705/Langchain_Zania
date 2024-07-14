# PDF Question Answering AI

This project is an AI agent that leverages OpenAI's large language model to extract answers from a PDF document and post the results on Slack.

## Features
- Extract text from a PDF document
- Answer questions based on the content of the document
- Post answers to a Slack channel

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Set up environment variables:
    ```sh
    export OPENAI_API_KEY=''
    export SLACK_API_TOKEN=''
    export SLACK_CHANNEL=''
    ```

3. Run the application:
    ```sh
    python src/main.py src/handbook.pdf "What is the name of the company?" "Who is the CEO of the company?" 
    python src/main.py src/handbook.pdf "What is their vacation policy?" "What is the termination policy?"
    ```


## Improvements
### Accuracy
- Fine-tune the LLM with domain-specific data.
- Implement more sophisticated text preprocessing and question understanding.

### Modularity and Scalability
- Use dependency injection to improve testability.
- Separate configuration from code using a configuration management tool.
- Implement logging and error handling.
- Add support for additional input formats (e.g., DOCX, TXT).
