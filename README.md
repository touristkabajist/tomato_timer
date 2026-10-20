# Tomato Timer

A simple desktop Pomodoro-style reminder app that helps you stay focused and get up from your desk on time.

## Why it exists

This project is designed for one purpose: remind you to take a break after a focused 30-minute work session. It pops up a window, asks you to confirm, and then counts down until the next break reminder.

## Features

- 30-minute countdown timer
- Always-on-top reminder popup
- Simple confirmation dialog
- Live countdown display in minutes and seconds
- Automatic restart after each cycle
- Lightweight Python + Tkinter desktop app

## Quick Start

```bash
python reminder_2.py
```

## Files

- `reminder_2.py` — main app
- `reminder_2.spec` — PyInstaller packaging config
- `reminder_1py` — earlier Windows message-box prototype
- `reminder_0.py` — basic reminder script

## Build Executable

```bash
pyinstaller reminder_2.spec
```

## How it works

1. Launch the app.
2. Confirm the reminder prompt.
3. The app starts a 30-minute countdown.
4. When time is up, it reminds you to stand up and take a break.
5. The cycle repeats automatically.

## Requirements

- Python 3
- Tkinter
- Windows recommended for desktop popup behavior

## Note

This is a lightweight personal productivity tool, built for quick reminders rather than a full-featured timer suite.
