#Tim Lucas
#Lab 10-2
#2025-07-01

def main():
    print("File Processor")
    print()

    file_name = input("Enter the name of the file you wish to process: ")

    try:
        with open(file_name) as file:
            text = file.read()   
        
            text = text.replace(".", "")
            text = text.replace(",", "")
            text = text.replace("\n", " ")

            word_list = text.split(" ")

            word_list = [word for word in word_list if word != ""]

            word_count = len(word_list)

            upper_count = 0

            for word in word_list:
                if word.istitle():
                    upper_count += 1
            
            print(f"The file {file_name} contains {word_count} words of which {upper_count} of them are capitalized.")


    except FileNotFoundError:
        print(f"The file \"{file_name}\" does not exist")




if __name__ == "__main__":
    main()