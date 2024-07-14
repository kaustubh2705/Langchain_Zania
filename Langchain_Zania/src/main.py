import sys
from pdf_parser import PDFParser
from question_answering import QuestionAnswering  # Ensure this is updated
from slack_client import SlackClient
from config import Config

def main(pdf_path, questions):
    config = Config()
    
    # Initialize the Slack client
    slack_client = SlackClient(config.slack_token, config.slack_channel)
    
    # Parse the PDF
    parser = PDFParser(pdf_path)
    document_text = parser.extract_text()
    
    # Answer the questions using QuestionAnswering class
    qa = QuestionAnswering(config.openai_api_key)
    answers = qa.answer_questions(document_text, questions)
    
    # Post the results to Slack
    slack_client.post_results(answers)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    questions = sys.argv[2:]
    main(pdf_path, questions)
