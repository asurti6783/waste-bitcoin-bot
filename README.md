## This is a Simple Bitcoin Notification bot for telegram

Extract the bot chat_ID via the following 
`https://api.telegram.org/<API-TOKEN>/getUpdates` in the response you will see the bot chat_id

We can use the bot in cron job, right now I am using the following cron job

```bash
0 */8 * * * python3 /root/waste-bitcoin-bot/notify.py
```
Every 2 hours:

```bash
0 */2 * * * python3 /root/waste-bitcoin-bot/notify.py
```
