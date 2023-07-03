import os

def clear_clutter(folder_path):
    # Create a list of all files in the folder
    file_list = os.listdir(folder_path)
    png_count = 0
    other_count = 0

    # Loop through each file in the folder
    for filename in file_list:
        # Check if the file is a PNG image
        if filename.lower().endswith('.png'):
            png_count += 1
            new_filename = str(png_count) + '.png'
        else:
            other_count += 1
            # Get the file extension and create a new filename
            file_extension = os.path.splitext(filename)[1]
            new_filename = str(other_count) + file_extension

        # Rename the file to the new filename
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

if __name__ == "__main__":
    folder_path = "D:\\100DaysofPython\\Day68\\files"  # Replace this with the actual path to your folder
    clear_clutter(folder_path)
