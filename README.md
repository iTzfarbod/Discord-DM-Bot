# Discord-DM-Bot
This Python bot allows you to forward direct messages received by the bot to the owner’s DMs. It’s a useful feature for keeping the bot owner informed about user interactions.

[![language](https://skillicons.dev/icons?i=py)](https://skillicons.dev)
## Features
-   Listens for direct messages in the bot’s DM channel.
-   Sends the received message to the bot owner’s DMs.
-   Easy setup and customization.

## Prerequisites
-   Python 3.6 or higher
-   discord.py library

## Installation
1 . Clone this repository to your local machine.

2 . Install the required dependencies using pip:
```powershell
pip install discord.py
```
3 . Create a new bot on the Discord Developer Portal.

4 . Copy your bot token.

5 . Replace `YOUR_BOT_TOKEN` in the `bot.run()` line of `Discord_Ticket_bot.py` with your actual bot token.

## Usage
1 . Invite your bot to your server.

2 . Run the bot using:
```powershell
python main.py
```

3 . When a user sends a direct message to the bot, the bot will forward it to the owner’s DMs.

## Configuration
-   Modify the `YOUR_USER_ID` variable in `Discord_Ticket_bot.py` to your `user ID` (the owner of the bot). You can find your `user ID` by enabling Developer Mode in Discord and right-clicking on your username.
-   Customize the bot’s prefix and other settings in `Discord_Ticket_bot.py`.

## Contributing
Feel free to contribute to this project by opening issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.




