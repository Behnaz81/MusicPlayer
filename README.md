# 🎵 Music Journal - Lyrics Translator and Audio Player

**Music Journal** is a lightweight web application built with Flask that allows users to:

- Search for a song by title and artist.
- Fetch lyrics from Genius.
- Automatically detect the lyrics' language.
- Translate English lyrics to Persian (Farsi).
- Display the lyrics line-by-line with translation.
- Play the associated audio file if available locally.

---

## ✨ Features

- 🎤 Fetch lyrics using the Genius API
- 🌍 Language detection with `langdetect`
- 🔁 English-to-Persian translation with `googletrans` (or optionally use AI APIs)
- 🔎 Match local audio files by metadata (ID3 tags)
- 🎧 Audio playback with HTML5 `<audio>` player
- 🖼 Display song cover image

---

## ⚙️ Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/music-journal.git
cd music-journal

# 2. Create a virtual environment (optional but recommended)
python -m venv .venv
# Activate:
source .venv/bin/activate       # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

---

## 🧠 Translation Options

This project uses `googletrans` by default, but you can integrate with:

- Hugging Face Transformers (`Helsinki-NLP/opus-mt-en-fa`)
- OpenAI API or DeepSeek API (requires API key)
- Any custom translation model

---

## 📁 Project Structure

```
music_journal/
│
├── static/
│   └── audio/            # MP3 audio files
│
├── templates/
│   ├── form.html         # User input form
│   └── result.html       # Result and lyrics view
│
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
└── README.md             # You're here!
```

---

## ✅ Dependencies

- Flask
- lyricsgenius
- googletrans
- langdetect
- mutagen

---

## 🔐 Note

You must provide your own **Genius API token** in the code to use the lyrics feature.

---

## 🧑‍💻 Author

Made with ❤️ by Behnaz

