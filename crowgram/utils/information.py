alive_usage = "🔌 Plugin Name: Alive\n\n📖 Description: This is used to check if Crowgram is alive.\n\n🪄 Usage: It is possible to know the status of Crowgram with the >alive command."

ping_usage = "🔌 Plugin Name: Ping\n\n📖 Description: Check how long it takes to ping Crowgram.\n\n🪄 Usage: Use the >ping command to find out how long it takes to ping Crowgram."

id_usage = "🔌 Plugin Name: ID\n\n📖 Description: It is used to know the Chat ID of the user and group.\n\n🪄 Usage: It is possible to get the chat ID of a user or group through the >id command."

protection_usage = "🔌 Plugin Name: Protection\n\n📖 Description: If an unknown person sends a private message without permission, that user will be blocked directly.\n\n🪄 Usage: If you want to allow an unknown user to send a private message, then use the following command to reply to that user's message.\n\nCommand: >a\n\nIf you want to remove the permission to send a private message to someone who has permission, then enter the following command in the reply to that user's message.\n\nCommand: >d"

restricted_usage = "🔌 Plugin Name: Restricted\n\n📖 Description: It is possible to save the content sent by the timer in a private message, and it is possible to download the restricted contents of a public, private group, or channel.\n\n🪄 Usage: If a user sends content with a timer in a private message, if you use the following command in the reply to that content, the content sent with a timer will be saved in saved messages.\n\nCommand:\n>rcd\n\nIt is possible to download those contents through the content link, which is restricted to the public or private group or channel. For this, you have to copy the link to that content and use the following command.\n\nFor restricted public groups and channels:\n>rcd -public url message_id\n\nFor restricted private groups and channels:\n>rcd -private group_id message_id"

logger_usage = "🔌 Plugin Name: Logger\n\n📖 Description: It is possible to keep logs of private messages and group messages.\n\n🪄 Usage: Crowgram will automatically log private messages and group messages; it requires mandatory log groups, or the logger will not work."

who_usage = "🔌 Plugin Name: Who\n\n📖 Description: It is possible to know the previous name and previous username of any user.\n\n🪄 Usage: The following command should be used to reply to the message of the user who needs to know the information.\n\nCommand: >who"

updater_usage = "🔌 Plugin Name: Updater\n\n📖 Description: Any new update of Crowgram can actually be updated to the new version.\n\n🪄 Usage: It is possible to use the new version of Crowgram through the >update command."

connect_usage = "🔌 Plugin Name: Connect\n\n💡 Recommend: Add your owner account to your assistant's contact list.\n\n📖 Description: Anyone can be allowed to use the music player through Connect, and they will be allowed to play, pause, resume, and end.\n\n🪄 Usage: If you want to allow someone else to use your Music Player, then execute the following command in the inbox of your Assistant account.\n>c -id user_id or >c -username @user_name"

disconnect_usage = "🔌 Plugin Name: Disconnect\n\n💡 Recommend: Add your owner account to your assistant's contact list.\n\n📖 Description: Disconnect will allow removing permission from Music Player for those already granted permission, who will lose Play, Pause, Resume, and End permissions.\n\n🪄 Usage: If you want to remove the assumption from someone who has permission to control the music player, you must execute the >r user_id command in the DM of the assistant account."

authorized_usage = "🔌 Plugin Name: Approve List\n\n📖 Description: It is possible to see the list of people who are allowed to use Music Player.\n\n🪄 Usage: If you want to see the list of those who are allowed to control the music player, execute the >l command in the DM of the assistant account."

play_usage = "🔌 Plugin Name: Play\n\n📖 Description: It is possible to listen to music from YouTube within a Telegram voice call, and it is possible to play music using the name of the favorite song or YouTube video link in a Telegram voice call.\n\n🪄 Usage: The name of the song or YouTube video link that you want to listen to should be added to the >play command.\nExample: >play song name or >play YouTube url"

vplay_usage = "🔌 Plugin Name: vPlay\n\n📖 Description: It is possible to listen to music from YouTube within a Telegram video call, and it is possible to play music using the name of the favorite song or YouTube video link in a Telegram video call.\n\n🪄 Usage: The name of the song or YouTube video link that you want to listen to should be added to the >vplay command.\nExample: >vplay song name or >vplay YouTube url"

pause_usage = "🔌 Plugin Name: Pause\n\n📖 Description: It is possible to control the music player using the voice call method of Telegram, and the music can be paused if desired.\n\n🪄 Usage: If the song needs to be paused, it can be paused only through the >pause command."

resume_usage = "🔌 Plugin Name: Resume\n\n📖 Description: It is possible to control the music player using the voice call method of Telegram, and the music can be resumed if desired.\n\n🪄 Usage: If the song needs to be resumed, it can be resumed only through the >resume command."

end_usage = "🔌 Plugin Name: End\n\n📖 Description: It is possible to control the music player using the voice call method of Telegram, and the music can be ended if desired.\n\n🪄 Usage: Just use the >end command to stop the song; streaming will be stopped by the >end command."