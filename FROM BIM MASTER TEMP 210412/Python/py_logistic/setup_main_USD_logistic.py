from distutils.core import setup
import py2exe

# setup(console=['main.py'])

#run command line: python setup_organize.py py2exe

# setup(
#     console = [
#         {
#             "script": "main.py",                    ### Main Python script    
#             "icon_resources": [(0, "icon.ico")]     ### Icon to embed into the PE file.
#         }
#     ],
# )

setup(
    console = [
        {
            "script": "main_USD_logistic.py"
        }
    ],
    options={
        'py2exe': 
        {
            'includes': ['lxml.etree', 'lxml._elementpath', 'gzip'],
        }
    }
)