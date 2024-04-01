from setuptools import setup, find_packages

setup(
    name='youtube_ocr',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pytesseract',
        'opencv-python',
        'python-pptx',
        'pytube',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'youtube-ocr = youtube_ocr.ocr:main'
        ]
    },
)
