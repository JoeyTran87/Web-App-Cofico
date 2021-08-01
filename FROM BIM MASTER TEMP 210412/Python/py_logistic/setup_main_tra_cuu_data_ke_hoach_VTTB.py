from distutils.core import setup
import py2exe
import shutil,os

# os.chdir(os.getcwd())
# path_root = os.getcwd()
# print(path_root)



# setup(console=['data_ke_hoach.py'])

#run command line: python setup_organize.py py2exe

setup(
    console = [
        {
            "script": "data_ke_hoach.py"
        }
    ],
    options={
        'py2exe': 
        {
            'includes': ['lxml.etree', 'lxml._elementpath', 'gzip'],
        }
    }
)

# setup(
#     windows=[{'script': 'data_ke_hoach.py'}],
#     options={
#         'py2exe': 
#         {
#             'includes': ['lxml.etree', 'lxml._elementpath', 'gzip'],
#         }
#     }
# )