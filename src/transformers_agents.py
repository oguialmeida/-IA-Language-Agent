from transformers import MBartForConditionalGeneration, AutoModelForCausalLM, MBart50TokenizerFast, BitsAndBytesConfig, AutoTokenizer
from dotenv import load_dotenv
import os

load_dotenv()

class Agents:

    def translate_text(origin_text: str, origin_lang: str, dest_lang: str) -> str:
        """
        Method to perform text translation using MBart.
        
        :param origin_text: Source text to be translated
        :param origin_lang: Source language of the text
        :param dest_lang: Target language for translation
        :return: Translated text
        """

        model_name = os.getenv('MBART_MODEL')
        if not model_name:
            raise ValueError("The model was not configured correctly. Check in .env.")

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
        return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    
    def generate_text(input_text: str):
        """
        Method to generet text using llama.
        
        :param input_text: Source text to base
        :return: generated text
        """

        # Configuração do modelo e quantização
        model_id = os.getenv("LLAMA_MODEL")
        quantization_config = BitsAndBytesConfig(load_in_8bit=True)

        # Carregando o modelo quantizado
        quantized_model = AutoModelForCausalLM.from_pretrained(
            model_id, device_map="auto", torch_dtype=torch.bfloat16, quantization_config=quantization_config
        )

        # Carregando o tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_id)

        # Tokenizando o texto de entrada
        input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

        # Gerando a saída do modelo
        output = quantized_model.generate(**input_ids, max_new_tokens=10)

        # Decodificando e retornando o resultado
        return tokenizer.decode(output[0], skip_special_tokens=True)

    
    def image_generator_agent():
        return
