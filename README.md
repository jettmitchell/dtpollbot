# dtpollbot
A twitch bot that can programmatically make polls and do things with the poll results

I am extremely rusty with python, so this is also a learning experiment! Suggestions welcome.

## Goals for dtpollbot:
* Create a poll with any number of options, triggered by function call
* Listen to Chat and save votes, accepting one vote per username
* End poll based on declared duration or by command from owner/moderator
* Create a web-page-based overlay that can be shown in OBS and other streaming software, which shows live feedback of the results so far, and a display of the final results when the poll closes
* A means of programmatically retreiving the results and triggering any follow-up functions using those results.



## Completed features:
Is present on hardcoded channel and listens to all incoming twitch messages.<br>
Creates poll (with hardcoded values) triggered by command typed into chat.<br>
Records messages relevant to the poll and discards all others.<br>
Accepts only 1 vote per username for each poll.<br>
Polls have a start time and an end time; automatically close poll after given duration.<br>



## To Do list:
Determine the results of the poll (count all valid votes for each option) and then report the winner (highest count)<br>
What happens if there’s a tie? (Probably let the script using the bot, like the D&D script, decide how to handle that)<br>
Accept command variables to create poll entirely from chat if desired<br>
Ensure that people using the !dtpoll command have permissions to do so<br>
Generate logfile of votes and past polls<br>
Use logfile to create overlay of results<br>
