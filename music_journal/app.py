from flask import Flask, render_template, request
from lyricsgenius import Genius
import re
import os
from mutagen.easyid3 import EasyID3
from langdetect import detect
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

def translate_en_to_fa(text):
    result = translator.translate(text, src='en', dest='fa')
    return result.text

def is_english(text):
    try:
        return detect(text) == "en"
    except:
        return False

def find_audio_by_metadata(artist, song_title, audio_dir="static\\audio"):
    artist = artist.lower()
    song_title = song_title.lower()
    best_match = None
    best_score = 0

    for root, dirs, files in os.walk(audio_dir):
        for file in files:
            if file.endswith(".mp3"):
                filepath = os.path.join(root, file)
                try:
                    tags = EasyID3(filepath)
                    file_artist = tags.get('artist', [''])[0].lower()
                    file_title = tags.get('title', [''])[0].lower()

                    score = 0
                    if artist in file_artist:
                        score += 1
                    if song_title in file_title:
                        score += 1

                    if score > best_score:
                        best_score = score
                        best_match = os.path.relpath(filepath, audio_dir)

                except Exception as e:
                    continue
    if best_match:
        return os.path.join("static\\audio", best_match)
    else:
        return None


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        genius = Genius("gYN09uR3NSsFl-7QfXUXzp95POoSFVUZ77KmCDqaMKRSCZZHTxvW1TBhXfvr9vRQ", timeout=15)
        artist = request.form["artist"]
        song_title=request.form["song_title"]
        song = genius.search_song(song_title, artist)
        audio_filename = find_audio_by_metadata(artist, song_title)
        has_audio = audio_filename is not None

        if song:
            raw_lyrics = song.lyrics

            split_index = raw_lyrics.find('[')
            if split_index != -1:
                cleaned_lyrics = raw_lyrics[split_index:]
            else:
                cleaned_lyrics = raw_lyrics

            cleaned_lyrics = re.sub(r'\[.*?\]', '', cleaned_lyrics)
            cleaned_lyrics = cleaned_lyrics.split("You might also like")[0].strip()
        else:
            cleaned_lyrics = "متاسفانه متن پیدا نشد."

        cover_url = song.song_art_image_url

        if re.search(r'[a-zA-Z]', cleaned_lyrics):
            text_direction = "ltr"
            text_align = "left"
        else:
            text_direction = "rtl"
            text_align = "right"

        english_lines = cleaned_lyrics.strip().split('\n')
        combined_lines = cleaned_lyrics

        is_lyrics_english = is_english(cleaned_lyrics)

        if is_lyrics_english:
            translation = translate_en_to_fa(cleaned_lyrics)
            translated_lines = translation.strip().split('\n')
            combined_lines = list(zip(english_lines, translated_lines))

        return render_template("result.html", song_title=song_title, artist=artist, lyrics=combined_lines, cover_url=cover_url, text_direction=text_direction, text_align=text_align, audio_filename=audio_filename, has_audio=has_audio, is_lyrics_english=is_lyrics_english)


    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
