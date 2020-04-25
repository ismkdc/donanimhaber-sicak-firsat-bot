crontab -l | { cat; echo "0 12 * * * python /home/donanimhaber-sicak-firsat-bot/bot.py"; } | crontab -
