import openai
import re

class QuestionAnswering:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def answer_questions(self, document_text, questions, chunk_size=3000):
        answers = {}
        document_chunks = self.split_text_into_chunks(document_text, chunk_size)
        
        for question in questions:
            all_answers = []
            for chunk in document_chunks:
                prompt = self.create_prompt(chunk, question)
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response.choices[0].message['content'].strip()
                if answer:
                    all_answers.append(answer)
            
            combined_answer = self.aggregate_answers(all_answers, question)
            if self.is_data_not_available(combined_answer):
                combined_answer = "Data Not Available"
            answers[question] = combined_answer
        return answers

    def create_prompt(self, document_text, question):
        prompt_template = """
        Based on the following document, answer the question as accurately as possible:

        Document: {document_text}

        Question: {question}
        """
        return prompt_template.format(document_text=document_text, question=question)
    
    def split_text_into_chunks(self, text, chunk_size):
        words = text.split()
        chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
        return chunks
    
    def aggregate_answers(self, answers, question):
        # print(answers)
        unique_answers = list(set(answers))
        
        # Summarize if there are multiple unique answers
        if len(unique_answers) == 1:
            return unique_answers[0]
        elif len(unique_answers) > 1:
            summary_prompt = f"Summarize the following answers into a single concise answer to the question '{question}':\n\n" + "\n\n".join(unique_answers)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": summary_prompt}
                ]
            )
            summary = response.choices[0].message['content'].strip()
            return summary
        
        return "Data Not Available"

    
    def is_data_not_available(self, answer):
        # Check for specific phrases indicating insufficient or non-specific answers
        if not answer or "not explicitly mentioned" in answer.lower() or "data not available" in answer.lower():
            return True
        
        return False

