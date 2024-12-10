from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from dotenv import load_dotenv
import os

load_dotenv()

def agent(origin_text, origin_lang, dest_lang):
    model_name = os.getenv('SECRET_MODEL')
    
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name, src_lang=origin_lang)

    model_inputs = tokenizer(origin_text, return_tensors="pt")

    # Translate from English to destiny language
    generated_tokens_pt = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[dest_lang]
    )
    print(tokenizer.batch_decode(generated_tokens_pt, skip_special_tokens=True))

if __name__ == "__main__":
    agent("Hello world!","en_XX","pt_XX")
