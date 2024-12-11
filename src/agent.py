# agent.py
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import os

def agent(origin_text: str, origin_lang: str, dest_lang: str) -> str:
    """
    Function to perform text translation using MBart.
    
    :param origin_text: Source text to be translated
    :param origin_lang: Source language of the text
    :param dest_lang: Target language for translation
    :return: Translated text
    """
    model_name = os.getenv('SECRET_MODEL')
    if not model_name:
        raise ValueError("The model was not configured correctly. Check SECRET_MODEL in .env.")

    # Load model and tokenizer
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name, src_lang=origin_lang)

    # Prepare input for the model
    model_inputs = tokenizer(origin_text, return_tensors="pt")

    # Translate to the target language
    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[dest_lang]
    )

    # Decode and return the translated text
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated_text
