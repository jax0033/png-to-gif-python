import imageio
import os

#duration for each frame
duration = input("Enter frame Duration (enter/skip for standard duration 0.035): ")
loop=True

if duration == "":
	duration = 0.035

while loop:
	try:
		duration = float(duration)
		loop=False
	except:
		duration = input("Invalid duration format, enter nothing, an float or an integer: ")

#output name
output = input("Enter gif Output Name: ")
aimages = []

#path to the workspace folder
path = "./workspace"

#creates a list of all filenames without extension
for image in os.listdir(path):
	aimages.append(int(image.split(".")[0]))

#sorts all the filenames by lowest to highest value 
done = 1
while done != 0:
	done = 0
	for i, n in enumerate(aimages):
		if i == len(aimages)-1:
			break
		else:
			if aimages[i] > aimages[i+1]:
				aimages[i], aimages[i+1] = aimages[i+1], aimages[i]
				done += 1

#path to the images in order
for n in range(len(aimages)):
	aimages[n] = path + "/" + str(aimages[n]) + ".png"

#creates the gif and saves it
images = list(map(lambda filename: imageio.imread(filename), aimages))
imageio.mimsave(str(output) + ".gif", images, duration=0.035)

#clears the workspace folder if y == true
clear_workspace = input("Gif creation complete. Clear workspace? (y/n)")

if clear_workspace == "y":
	for file in os.listdir(path):
		os.remove(path+"/"+file)

"""
									created by jax0033@protonmail.com
"""