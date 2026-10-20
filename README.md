# Tomato Timer

A simple desktop reminder app inspired by the Pomodoro technique. The program opens a topmost popup window, asks whether to start a fresh 30-minute countdown, and then shows a running countdown until time is up. When the timer ends, it prompts the user to take a short break and starts again.

This project is a lightweight Python/Tkinter app designed for Windows desktop use.

## Features

- 30-minute countdown timer
- Popup reminder window that stays on top of other apps
- Confirmation dialog before starting each cycle
- Countdown display with minutes and seconds
- Automatic restart after each completed session
- Simple and portable Python implementation

## Project Files

- `reminder_2.py` — main application
- `reminder_2.spec` — PyInstaller spec file for packaging an executable
- `reminder_1py` — earlier prototype using Windows `ctypes` message box
- `reminder_0.py` — minimal test/reminder script

## How it works

The app creates a Tkinter window and hides the main root window. It then shows a custom dialog asking:

- “休息时间到啦！站起来走走吧QwQ”
- “是否进入30分钟倒计时?”

If the user confirms, the application starts a countdown of 1800 seconds (`30 * 60`) and updates the visible label once per second. When the timer reaches zero, it destroys the countdown window and starts the reminder flow again.

## Requirements

- Python 3.x
- Tkinter (usually included with Python on Windows)
- Windows environment recommended for the desktop popup behavior

## Run it locally

```bash
python reminder_2.py
```

If Tkinter is not installed, you may need to install it via your Python distribution or package manager.

## Build an executable

This project includes a PyInstaller configuration file:

```bash
pyinstaller reminder_2.spec
```

This will generate a packaged Windows executable in the build output directory.

## Example usage

1. Launch the app.
2. Confirm the reminder prompt.
3. Work until the timer ends.
4. Take a short break.
5. Repeat the cycle.

## Notes

- The app is intentionally simple and not a full productivity suite.
- It is best suited for personal focus sessions and quick reminders.
- Some files in the repository are earlier experiments and prototypes rather than the final version.

## License

No explicit license file was found in the repository, so the project is provided as-is without a formal license declaration.
