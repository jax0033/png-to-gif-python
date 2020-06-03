import os

path = "./workspace/"

for file in os.listdir(path):
	os.remove(path+file)