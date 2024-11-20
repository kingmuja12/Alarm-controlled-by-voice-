# Alarm Scheduler with Sound Alerts and Speech-to-Text Command

This Python script, `main.py`, schedules alarms, plays random alarm sounds, and listens for user commands to stop the alarms. It uses background scheduling, threading, and speech-to-text transcription for dynamic control.

## Features
- Schedule alarms with start and end times.
- Play a random alarm sound during the scheduled time.
- Stop alarms dynamically using voice commands ("stop").
- Supports background scheduling and multiple job management.

## Prerequisites
- Python 3.7 or higher
- Required Python libraries:
  - `pygame`
  - `apscheduler`
  - `speech_to_text` (custom or third-party module for transcription)
- A folder containing alarm sound files.

## Setup
1. Clone or download the repository.
2. Ensure the required dependencies are installed (see `requirements.txt`).
3. Add your alarm sound files to a folder and update the `list_of_sound` variable in `main.py` with the file paths.

## Installation
1. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
