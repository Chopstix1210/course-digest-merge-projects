import argparse
import os
import shutil
import subprocess
import sys


def clear_dir(dir: str):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        try:
            shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete file. Go talk to Kevin about error {e}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--Folder", help="Folder containing unzipped projects")

    args = parser.parse_args()

    if not args.Folder:
        print(
            'Please include the folder where the unzipped project files are contained. \n Use the -o flag with " /path/to/file ".'
        )

    try:
        folder_path = os.path.abspath(args.Folder)
        correct_path = input(f"\nIs this is the correct path: {folder_path}? [y/n]")
        if correct_path != "y":
            print(
                "No worries. Run the script again with the correct path. Or go bother Kevin if the path continues to fail."
            )
            return -1
    except Exception as e:
        print(
            f"File Path {args.Folder} does not exists. Please correct the pathing. The path can be a relative path."
        )
        return -1

    print(
        "\nI'm going to show you  the first two files of the folder. If these do not look correct please abort by using CTRL-C\n"
    )
    try:
        files = os.listdir(folder_path)
        print(files[:2])
        correct_files = input("Are these the correct files? [y/n]")
        if correct_files != "y":
            ds_store = input("Does your folder include .DS_store? [y/n]")
            if ds_store == "y":
                print("No worries... I'm deleting that right now")
                print(f"{folder_path}/.DS_Store")
                os.remove(f"{folder_path}/.DS_Store")
                print("DS.store removed! Printing new two folders.")
                files = os.listdir(folder_path)
                print(files[:2])
                correct_files = input("Are these the correct files? [y/n]")
                if correct_files != "y":
                    print(
                        "No worries... I'm aborting the operation and you can try again. Or go repremand Kevin. Your choice!"
                    )
            elif ds_store != "y":
                print(
                    "No worries... I'm aborting the operation and you can try again. Or go repremand Kevin. Your choice!"
                )
            return -1
    except Exception as e:
        print(f"Error: {e}")
        print(
            "Something went wrong with getting all the files in the folder. If this continues to happen go yell at Kevin for his mistakes"
        )
        return -1

    permission = input(
        "Do I have permission to make two new folders while the merging occurs? You can delete them afterwards. [y/n]"
    )
    if permission != "y":
        print(
            "No worries at all. Talk with Mia or Kevin to see what can be done about this."
        )
        return -1

    print(
        "\nSounds good!\nI will now start merging the projects together... Kevin isn't a good developer so his code is really slow and runs at O(kn/2 +1). While you wait go tell him this code sucks!"
    )

    # initializing end pointer (index not really a pointer)
    j = len(files) - 1
    try:
        print("Creating new directories...")
        os.mkdir("./temp")
        os.mkdir("./output")
        print("Directories Created")
    except Exception as e:
        print(f"Error: {e}")
        print(
            "Something went wrong with creating the directory. I'll print the error, but usually the error is due to there already being the directories temp and output in the root"
        )

    try:
        print("Copying files to the temp directory")
        shutil.copytree(folder_path, "./temp", dirs_exist_ok=True)
        print("Files have been copied. Contuining with the rest of the merging")
    except Exception as e:
        print(f"Error occurred: {e}")
        print(
            "An error occured while copying the the data from the original folder. Talk with Kevin to get this resolved"
        )
        return -1

    output_len = len(os.listdir("./output"))

    while output_len != 1:
        print(len(os.listdir("./temp")))
        j = len(os.listdir("./temp")) - 1
        if j == -1:
            break
        if len(os.listdir("./output")) > 0:
            clear_dir("./output")
        for i in range(len(os.listdir("./temp"))):
            print(f"j:{j} -- i:{i}")
            temp_files = os.listdir("./temp")
            print(temp_files)
            if ".DS_Store" in temp_files:
                os.remove("./temp/.DS_Store")
                temp_files = os.listdir("./temp")
                j -= 1
            if i == j:
                os.mkdir(f"./output/output_project_{i}")
                shutil.copytree(
                    f"./temp/{temp_files[i]}",
                    f"./output/output_project_{i}",
                    dirs_exist_ok=True,
                )
            elif i < j:
                mergea = os.path.abspath(f"./temp/{temp_files[i]}")
                mergeb = os.path.abspath(f"./temp/{temp_files[j]}")
                os.mkdir(f"./output/output_project_{i}")
                output_dir = os.path.abspath(f"./output/output_project_{i}")
                npm_command = f"npm run start -- --operation merge --mergePathA {mergea} --mergePathB {mergeb} --outputDir {output_dir}"
                # print(npm_command)
                # os.system(command=npm_command)
                subprocess.run(
                    npm_command.split(),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            j -= 1
        output_len = len(os.listdir("./output"))

        clear_dir("./temp")
        shutil.copytree("./output", "./temp", dirs_exist_ok=True)

    print(
        f"Project is done merging.\n You can find the project output file in ./output"
    )

    return 0


if __name__ == "__main__":
    return_int = main()
