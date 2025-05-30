import os

readme_content = """\
## Projekt aplikacji CleanApp ma na celu demonstrację umiejętności pracy zespołowej.
Skład zespołu:  
- *Adrian Harasimczuk* - programista i lider zespołu  
- *Adrianna Gorzkowska* - specjalista działu księgowości i PR  
- *Jakub Kacpura* - uczy się, robi dobrą kawę  
- *Adrian Tabaczek* - coś tam testuje  

> [!IMPORTANT]  
> Zespół jest częścią grupy **_WEL24EX1N4_**
"""

gitignore_content = """\
# (PRZYKŁADOWY DLA ANDROIDA Z PIERWSZEJ LEPSZEJ KOLEKCJI TEMPLATEK)
# Gradle files
.gradle/
build/

# Local configuration file (sdk path, etc)
local.properties

# Log/OS Files
*.log

# Android Studio generated files and folders
captures/
.externalNativeBuild/
.cxx/
*.apk
output-metadata.json

# IntelliJ
*.iml
.idea/
misc.xml
deploymentTargetDropDown.xml
render.experimental.xml

# Keystore files
*.jks
*.keystore

# Google Services (e.g. APIs or Firebase)
google-services.json

# Android Profiling
*.hprof
"""

requirements_content = """\
backoff==2.2.1
InquirerPy==0.3.4
lxml==4.9.3
openai
jsonlines
numpy
protobuf
BeautifulSoup4
toml
aioconsole
python-dotenv
gymnasium
Pillow
evaluate
types-tqdm
tiktoken
aiolimiter
beartype==0.12.0
flask
nltk
text-generation
opencv-python

argparse
colorama
dashscope
pyshine
pyyaml
requests
Levenshtein
zhipuai
xmltodict
google.auth
docker
fuzzywuzzy
openpyxl
"""

def init_project():
    files = {
        'README.md': readme_content,
        '.gitignore': gitignore_content,
        'requirements.txt': requirements_content,
    }

    for file_name, content in files.items():
        with open(file_name, 'w') as f:
            f.write(content)

    print("Inicjalizacja projektu zakończona w bieżącym katalogu.")

if __name__ == '__main__':
    init_project()
