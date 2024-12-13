# IA Agent API with FastAPI and Transformers

This project is a **Multi-agent-back-end** designed to provide advanced text using a transformer-based language model.

1. **Transformers Agents**: A Python-based code that performs several agents with different functionalities.
2. **Fast API**: A lightweight API that receives user input, processes it, and communicates with the transformer agent to returns a translated text for example.

## Project Structure (Example with a Translate Model)

### Transformer Agent
- **Language Translation Engine**: Built using Python and Hugging Face Transformers.
- **Translation Logic**: Processes input text and translates it to the desired language.

### API
- **Endpoints**:
  - `POST /translate`: Accepts text input and target language parameters.
  - `GET /status`: Checks the API's operational status.
- **Middleware**: Includes input validation and error handling.
- **Communication**: Sends translation requests to the Python agent with HTTP.

### Install
```bash
python -m venv venv
source venv/Scripts/activate (Windows)
source venv/bin/activate (Linux/Mac)
pip install transformers torch protobuf sentencepiece tiktoken python-dotenv fastapi[standard] uvicorn
```

### To run (Windows)
```bash
python run_scripts.py
```

### To run (Linux/Mac)
```bash
uvicorn main:app --reload
```

### JSON Request example (Portuguese to English)
```bash
{
    "origin_text": "Esse gordo diz mentiras.",
    "origin_lang": "pt_XX",
    "dest_lang": "en_XX"
}
```
### The output shold bee

```bash
{
    "translated_text": "That fat guy's lying."
}
```

## Observations
The way things are translated will depend on the AI ​​model you are using, some may not be as accurate in their training.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or feature suggestions.

## License
[Hugging Face](https://huggingface.co/) is one of the most innovative and influential platforms for those working with AI, especially NLP, making the use of advanced models more accessible to developers and researchers. All AI models and similar libraries from this application were found there.
