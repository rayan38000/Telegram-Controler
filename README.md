# 🤖 Telegram Advertising Bot

**A bot designed to automate the posting of advertisements in various Telegram groups.**  
This project, called "Telegram Controler," uses Telegram's API to send advertising messages with media files to specific groups.

---

## ✨ Features

- **Automated Posting**: The bot publishes a predefined message in a list of Telegram groups.
- **Multimedia Support**: You can attach media files (images, videos, etc.) to your posts.
- **Message Customization**: The advertising message can be easily modified from a text file.
- **Group Management**: The list of targeted groups is retrieved from a text file.
- **Customizable Wait Time**: Set a delay between each post to avoid excessive spamming.
- **Timestamps**: Each post is timestamped with the local date and time in France for precise tracking.

---

## 🛠️ Installation

1. **Clone the project**:
   ```bash
   git clone https://github.com/yourrepo/TelegramAdvertisingBot.git
   cd TelegramAdvertisingBot
   ```

2. **Install dependencies**:  
   Make sure you have `Python` and `pip` installed, then run the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Telegram account**:
   Get your API credentials from the [Telegram Developer Portal](https://my.telegram.org/auth) and get the following information: `API_ID`, `API_HASH`, `PHONE_NUMBER`.

---

## 🚀 Running the Bot

1. **Prepare the configuration files**:
   - **Groups**: The list of groups where you want to send messages should be in `advertisingGroups.txt` (one link or username per line).
   - **Message**: The content of the advertising message should be in `advertisingMsg.txt`.
   - **Media**: Place your media files (optional) in the `media/` folder.

2. **Start the bot**:
   Run the script with the following command:
   ```bash
   python bot.py
   ```

3. **Track actions**:
   - You'll see the messages being posted to the groups and any errors that occur.
   - Each message will be timestamped with the local French time.

---

## 📄 Configuration Files

- **advertisingGroups.txt**: List of targeted groups (one per line, e.g., `https://t.me/groupname`).
- **advertisingMsg.txt**: Contains the message to be sent to the groups.
- **media/**: Folder where you place files (images, videos, etc.) to attach to the messages.

---

## 📋 Usage Example

- **Running the bot**: The bot fetches the group list from `advertisingGroups.txt`, reads the message from `advertisingMsg.txt`, and posts to each group with a delay between posts.
- **Adding media**: If files are present in the `media/` folder, they will be sent along with the message.

---

## ⚙️ Customization

- **Cooldown time**: The wait time between each post can be adjusted by modifying the `cooldown` variable in the script.
- **Media list**: The bot will send all files in the `media/` folder. You can easily add or remove files.

---

## 🤖 Technologies Used

- **Python**: Main language used for developing the bot.
- **Telethon**: Python library to interact with the Telegram API.
- **Pystyle & Colorama**: For styling console output.

---

## ⚠️ Disclaimer

Abusing this bot may result in your Telegram account being suspended. Please use it responsibly and adhere to Telegram's policies.

---

## 📞 Support

If you encounter any issues or have questions, feel free to create an issue on the repository or [contact me on Telegram](https://t.me/rayan960).
