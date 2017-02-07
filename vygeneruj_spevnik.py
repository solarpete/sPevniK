import sys, os

# Pre-written text to be copied to output html file:
output_file_intro = '''<!doctype html>
<html lang="sk">
  <head>
    <meta charset="UTF-8" />
    <meta name="author" content="Peter Korenciak" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>Želvov spevník v0.5</title>
    
    <!-- definicia internal CSS stylov: -->
    <style>
      body{
        font-size: 100%;
      }
      <!-- pre {font-size: 120%;} -->
      <!-- article{background-color: #FFE4C4} -->
      article{
        <!-- background-color: #FFFFF0; -->
        <!-- border-style: ridge; -->
        <!-- border-radius: 8px; -->
      }
      .akordy{
        color:blue;
        font-weight: bold;
      }
      .c_strany{
        text-align: center;
      }
      .interpret{
        font-variant: small-caps;
      }
      .pismena_indexu{color:magenta;}
      pre{
        margin: auto;
      }
      
      .spacer{
        margin-left: 10px;
      }
    </style>
  </head>

<body>
  <h1>Želvov spevník</h1>
  <p title="Verzia dokumentu">Verzia: 0.4</p>
  <h2>Úvod</h2>
  <p>V tomto spevníku nájdete všetky pesničky, ktoré viem alebo chcem vedieť hrať.</p>
  <p>Okrem toho spevník obsahuje 3 cool veci:
  <ul>
    <li><a href="#index_p_mena">index podľa mena interpreta</a>,</li>
    <li><a href="#index_p_priezv">index podľa priezviska interpreta</a>,</li>
    <li><a href="#index_p_nazvu">index podľa názvu piesne</a>.</li>
  </ul>
  
  Takže by nemal byť problém rýchlo nájsť pesničku, ktorú chcete (samozrejme ak
  tu je :-)).
  </p>
  
  <h2>Obsah</h2>
  <h2>Piesne</h2>
'''
output_file_outro = '''</body>
</html>
'''

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
song_number = 0
input_file_contents
for input_line in input_file_contents:
    if input_line == "{new_song}\n":
        song_number += 1
        print('Current song number: ' + str(song_number))
output_file.write(output_file_intro)
output_file.write(output_file_outro)
# output_file.write(input_file_contents[0])
# output_file.write(input_file_contents[1])
# print(input_file.read())


###########
# Cleanup:
###########
# Close the open files:
input_file.close()
output_file.close()

# while True:
    # print('Type exit to exit')
    # response = input()
    # if response == 'exit':
        # sys.exit()
    # print('You typed ' + response + '.')
