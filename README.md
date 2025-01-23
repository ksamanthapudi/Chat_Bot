# Chatbot Using Cornell Movie-Dialogs Corpus

This project demonstrates the development of a chatbot trained on the Cornell Movie-Dialogs Corpus. The chatbot can simulate natural language responses based on the input provided by users, offering an interactive experience.

---

## Features

- **Natural Language Processing**: Utilizes PyTorch for model training and response generation.
- **Cornell Movie-Dialogs Corpus**: Trained on a rich dataset containing conversations from movie scripts.
- **Flask Integration**: A web-based chatbot interface built using Flask and JavaScript.
- **Interactive UI**: Chatbot pops up on the page with smooth animations and typing effects.

---

## Project Structure

### 1. Corpus Data
- **Files Used**:
  - `movie_lines.txt`: Contains individual lines of dialogue.
  - `movie_conversations.txt`: Defines the conversation sequences using `movie_lines.txt`.
  - `movie_titles_metadata.txt`: Metadata about movies.

### 2. Model Training
- **Framework**: PyTorch
- **Files**:
  - `copy_of_updated_chatbot.py`: Contains the chatbot logic, training pipeline, and Flask API.
  - Trained models are saved as `trained_models.pth` in the `checkpoints` directory.

### 3. Frontend
- **HTML and JavaScript**:
  - Interactive chatbot interface for user input and display of responses.
  - Animated UI with a toggleable chatbot pop-up.

### 4. Backend
- **Flask API**:
  - Route `/api/chat` handles POST requests to generate responses.
  - Implements a GreedySearchDecoder for response generation.

---

## Installation Guide

### Prerequisites
1. Python 3.12
2. Pip

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   If `torch` fails, manually install a compatible version:
   ```bash
   pip install https://download.pytorch.org/whl/cpu/torch-2.0.1%2Bcpu-cp312-cp312-win_amd64.whl
   ```

4. **Prepare the Dataset**:
   - Ensure `movie_lines.txt` and `movie_conversations.txt` are placed in the working directory.

5. **Train the Model**:
   ```bash
   python copy_of_updated_chatbot.py
   ```
   (This script trains and saves the models in the `checkpoints` directory.)

6. **Run the Flask Server**:
   ```bash
   flask run
   ```

---

## Usage

1. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

2. Interact with the chatbot by typing your message into the input box.

---

## Technical Details

### Dataset Processing
- **Cleaning**: The dialogue lines are cleaned by removing special characters and standardizing contractions.
- **Pairing**: Pairs of conversations are extracted from `movie_conversations.txt` and `movie_lines.txt`.

### Model Details
- **Encoder**: A bidirectional GRU that encodes input sentences into context vectors.
- **Decoder**: A Luong Attention-based decoder that generates responses using context vectors.
- **Training**:
  - Optimized using Adam optimizer.
  - Teacher forcing applied during training.

### Flask API
- **Endpoints**:
  - `/`: Serves the chatbot UI.
  - `/api/chat`: Processes user input and returns bot responses.

---

## Troubleshooting

### Common Issues
1. **Package Not Found**:
   - Ensure you’ve installed dependencies using `pip install -r requirements.txt`.

2. **Torch Import Error**:
   - Install a compatible version of `torch` for your Python version.

3. **Dataset Missing**:
   - Ensure the Cornell Movie-Dialogs Corpus files are placed in the correct location.

---

## Future Improvements

- Enhance response quality by fine-tuning the model on additional datasets.
- Implement advanced attention mechanisms for better context understanding.
- Add a database to log and analyze user interactions.

---

## Acknowledgments
- **Dataset**: [Cornell Movie-Dialogs Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)
- **Libraries**: PyTorch, Flask, JavaScript (Frontend).
- **Authors**: Cristian Danescu-Niculescu-Mizil and Lillian Lee.

---


