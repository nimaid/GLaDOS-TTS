from typing import Optional

from ollama import chat

MODEL = "llama3.2"
PROMPT = "You are a text correction program who's sole job is to intelligently correct the spelling and punctuation of messages I send you. You must correct the errors in my messages, and respond ONLY with the corrected text. Do NOT shorten my ideas, remove my words, or paraphrase my thoughts. You must keep the content of my message unchanged, and simply correct the errors related to spelling and punctuation. If I make a word all uppercase LIKE THIS you must keep the word all uppercase while still correcting any punctuation or spelling errors. If I use an exclamation point at the end of a sentence, you must keep it as an exclamation point, and must not change it to a period. Here are some examples: If I say \"Wow, thats prety cool!\", you would respond \"Wow, that's pretty cool!\" If I say \"Is it REALY so bad if that hapens>\", you would respond \"Is it REALLY so bad if that happens?\" If I say \"whst do you wanr from that, REALLY?\", you would respond \"What do you want from that, REALLY?\" If you understand your role and are ready to start, respond to all of my following messages with your text corrections."

class LlamaChecker:
    def __init__(self, model: Optional[str] = MODEL, prompt: Optional[str] = PROMPT):
        self.model = model
        self.prompt = prompt
        
        self.messages = [
            {
                "role": "user",
                "content": self.prompt
            }
        ]
    
    def correct_text(self, text: str) -> str:
        this_messages = self.messages + [
            {
                "role": "user",
                "content": text
            }
        ]
        
        response = chat(model=self.model, messages=this_messages)
        return response.message.content
