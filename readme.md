# Language Translation API with Node.js and Transformers

This project is a **Language Translation System** designed to provide advanced text translation capabilities using a transformer-based language model. The system consists of two main components:

1. **Transformer Agent**: A Python-based backend that performs the actual language translation.
2. **Node.js API**: A lightweight API that receives user input, processes it, and communicates with the transformer agent to return translated text.

## Project Structure

### Transformer Agent
- **Language Translation Engine**: Built using Python and Hugging Face Transformers.
- **Translation Logic**: Processes input text and translates it to the desired language.

### Node.js API
- **Endpoints**:
  - `POST /translate`: Accepts text input and target language parameters.
  - `GET /status`: Checks the API's operational status.
- **Middleware**: Includes input validation and error handling.
- **Communication**: Sends translation requests to the Python agent with HTTP.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or feature suggestions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

