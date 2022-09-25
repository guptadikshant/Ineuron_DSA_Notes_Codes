def search(arr, ele):
	for i in range(len(arr)):
		if arr[i] == ele:
			return i
	else:
		return -1

if __name__ == "__main__":
	print(search(arr=[20,45,27, 47,55,67,75,88,90],ele=95))