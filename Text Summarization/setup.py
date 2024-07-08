import setuptools

# with open("README.MD", "r", encoding="utf-8") as f:
#     long_description = f.read()

__version__ = "0.0.0"
# Repo_Name = "Text Summarize"
# Author = "Welly"
Src_Repo = "textSummarizer"

setuptools.setup(
    name= Src_Repo,
    version= __version__,
    description="NLP app",
    url="https://github.com/DoomedMean/Machine-Learning/tree/main/Text%20Summarization",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)