import requests
import time

headers = {"authorization": "token"}
channel_IDs = ["List of channel ID's"]

file = open("text.txt", "r")
lines = file.readlines()

for i in range(100):
	for id in channel_IDs:
		for line in lines:
			requests.post(f"https://discord.com/api/v9/channels/{id}/messages", headers = headers, json = {"content": line})
		print("done")
		time.sleep(3)
