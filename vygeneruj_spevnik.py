import sys, os

# Globals:
default_input_file = 'spevnik_PK.cho'   # Experimental
default_output_file = 'spevnik_1.html'  # Temporary - po case to zmenim na
                                        # sPevniK.html, ked sa to bude aspon
                                        # trochu podobat na html :-)

                                        
# Experimental: If there is a file spevnik_PK.cho, then open the file (to save 
# time writing command line arguments all the time):
filenames = os.listdir(os.getcwd())
if default_input_file in filenames:
    print('File should be opened now.')
    input_file = open(default_input_file, 'r', encoding="utf8")
else:
    print('Error: File ' + default_input_file + 'not found. Exiting.')
    sys.exit()
# Note the section above can be updated to find all files with e.g. .cho suffix
# and to give user an option to include them in the resulting file.

# Open output file:
if default_output_file in filenames:
    print('Are you sure you want to overwrite your file ' + default_output_file
          + '? [Y/N]')
    response = input()
    if response == 'N':
        print('You typed ' + response + '. The program will now finish. If you \
               want to use non-default file you must specify the desired \
               filename as a second parameter.')    # TBD: Make changes, so that
               # it really works that way
        sys.exit()
print('Results will be written to: ' + os.path.abspath('.') + '\\' + default_output_file)
output_file = open(default_output_file, 'w', encoding="utf8")



input_file_contents = input_file.readlines()
output_file.write(input_file_contents[0])
output_file.write(input_file_contents[1])
# print(input_file.read())


###########
# Cleanup:
###########
# Close the open files:
input_file.close()
output_file.close()

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
