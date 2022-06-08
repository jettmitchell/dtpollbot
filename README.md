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
☑ Is present on hardcoded channel and listens to all incoming twitch messages.<br>
☑ Creates poll triggered by command typed into chat.<br>
☑ Records messages relevant to the poll and discards all others.<br>
☑ Accepts only 1 vote per username for each poll.<br>
☑ Poll ends automatically after given duration.<br>
☑ Results of poll are printed by the bot in chat.<br>



## To Do list:
☐ What happens if there’s a tie? (Probably let the script using the bot, like the D&D script, decide how to handle that)<br>
☐ Ensure that people using the !dtpoll command have permissions to do so<br>
☐ Generate logfile of votes and past polls<br>
☐ Use logfile to create overlay of results<br>
