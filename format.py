import os

path = "./workspace/"

n = 0

for file in os.listdir(path):
	n += 1
	os.rename(path+file, path + str(n) + ".png")

"""
									created by jax0033@protonmail.com
"""