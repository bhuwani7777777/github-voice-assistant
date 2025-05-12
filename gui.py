from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from voice_assistant import listen, speak
from github_api import get_issues

class ChatBotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitHub Voice Bot")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.chatBox = QTextEdit()
        self.chatBox.setReadOnly(True)

        self.listenButton = QPushButton("🎤 Speak")
        self.listenButton.clicked.connect(self.handle_command)

        layout.addWidget(self.chatBox)
        layout.addWidget(self.listenButton)
        self.setLayout(layout)

    def handle_command(self):
        command = listen()
        self.chatBox.append(f"👤 You: {command}")

        if "issue" in command or "issues" in command:
            issues = get_issues("octocat", "Hello-World")  # Change repo here
            response = "\n".join(issues)
        else:
            response = "Try saying: 'Get issues for Hello-World repository'."

        self.chatBox.append(f"🤖 Bot: {response}")
        speak(response)
