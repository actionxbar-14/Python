
import os 


#----> function for creating a file
def create_file(filename):
    try:
        with open(filename , 'x') as f:
            print(f"File Name {filename} : Created succussfully!")

    except FileExistsError:
        print(f"File name {filename} already exists!")


    except Exception as E:
        print("An error occurred!")



#-----> function to view all files
def view_all_files():
    files = os.listdir()
    if not files:
        print('No file found!')

    else:
        print('Files in directory!')
        for file in files:
            print(file)

        


#-----> function to delete a file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted succussfully!")

    
    except FileNotFoundError:
        print('File not found')

    except Exception as e:
        print('An error occoured!')





#------> function to read a file
def read_file(filename):
    try:
        with open(r"C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Projects\P11_File_Manager\sample.txt" , 'r') as f:
            content = f.read()
            print(f"Content of {filename} : \n {content}")
            

    except FileNotFoundError:
        print(f"{filename} does not exist!")

    
    except Exception as e:
        print('An error occurred!')




#------> function to edit a file
def edit_file(filename):
    try:
         with open(r"C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Projects\P11_File_Manager\sample.txt" , 'r') as f:
            content = input("Enter data to add : ")
            f.write(content + "\n")
            print(f"Content added to {filename} succussfully!")



    except FileNotFoundError:
        print(f"{filename} doesn't exist!")


    except Exception as e:
        print('An error occurred!')

    



# -----> main function

def main():

    while True:


        print("_____FILE MANAGEMENT APP_____")
        print('1 : Create file')
        print('2 : View all file')
        print('3 : Delete file')
        print('4 : Read file')
        print('5 : Edit file')
        print('6 : Exit Program')

        choice = input('Enter Your choice (1 - 6) : ')

        if choice == '1':
            filename = input('Enter the file-name to create : ')
            create_file(filename)


        elif choice == '2':
            view_all_files()


        elif choice == '3':
            filename = input("Enter the name of file you want to delete :")
            delete_file(filename)


        elif choice == '4':
            filename = input('Enter file name to read : ')
            read_file(filename)


        elif choice == '5':
            filename = input('Enter file name to edit :')
            edit_file(filename)



        elif choice == '6':
            print('Closing the File Manager program....')
            break 
        
        else:
            print('In-valid syntax')






# if '__name__' == '__main__':
main()


       






    

