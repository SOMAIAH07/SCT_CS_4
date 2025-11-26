# SCT_CS_4
TASK-04

Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file

⚠️ EDUCATIONAL KEYLOGGER (Cybersecurity Learning Tool Only)
⚠️ Disclaimer (Read First!)

This project is strictly for educational and cybersecurity learning purposes.
A keylogger can record every key a user types—including passwords, messages, and sensitive data.

❗ Using a keylogger on any device you do not own or do not have explicit written permission to test is illegal.
❗ Distributing, deploying, or running this program on someone else’s computer is a criminal offense in many countries.
❗ This is provided ONLY to help students understand how monitoring tools work in cybersecurity.

🎓 Project Overview

This example demonstrates how a keylogger conceptually works by using Python’s pynput library to detect key presses and log them to a file.

It is meant for:

Cybersecurity education

Understanding input monitoring

Learning about defensive strategies

Demonstrating how keylogging attacks occur so they can be better prevented

🚫 Not for real-world deployment
🚫 Not for monitoring others
🚫 Not for penetration testing without authorization

🧠 How It Works (Educational Explanation)

The script:

Listens for keyboard events.

Records:

Normal characters

Special keys (Enter, Space, Shift, etc.)

Logs the output into a local text file (keylog.txt).

Stops safely when the ESC key is pressed.

This helps students understand:

Keyboard event hooks

Logging mechanisms

How attackers capture input

Why secure systems must defend against such threats

📌 Requirements
pip install pynput


You must run this script only on a system you own.

🛡️ Defense & Prevention (Important Learning Component)

Modern systems protect against keyloggers using:

Antivirus & anti-malware detection

Keystroke encryption

Behavior monitoring

Secure input fields

Privilege isolation

Sandboxing

Studying simple examples like this helps learners understand how to design stronger defenses.

📁 Log File

All captured keystrokes (on your own device) are written to:

keylog.txt

📝 Ethical Usage Guidelines

✔ Allowed:

Learning how keyloggers work

Understanding cybersecurity vulnerabilities

Running the program only on your own personal machine

Academic research and cybersecurity assignments

❌ Not allowed:

Running on someone else’s device

Collecting data from others

Using it for spying, monitoring, or unauthorized access

Deploying it in any disguised or malicious way

Unauthorized use is illegal and punishable under cybercrime laws.
