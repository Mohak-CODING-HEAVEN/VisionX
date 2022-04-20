from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="VisionX",
    version="1.0.0",
    description="VisionX is a Python package to make it easy to run Image processing and other AI functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/Mohak-CODING-HEAVEN/VisionX",
    author="Mohak Bajaj",
    author_email="bmohak87@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Computer Vision :: Helper Library',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    keywords="visionx visionx-ai Image-Processing AI OpenCV Mediapipe ComputerVision HandTracking FaceTracking PoseEstimation",
    package_dir={"": "src"},
    packages=find_packages(where="visionx"),
    python_requires=">=3.7",
    install_requires=[
        "opencv-python",
        "mediapipe",
        "numpy"
    ],
    fullname="VisionX",
    project_urls={
        "Source": "https://www.github.com/Mohak-CODING-HEAVEN/VisionX",
        "Documentation": "https://www.github.com/Mohak-CODING-HEAVEN/VisionX/wiki",
        "Tracker": "https://www.github.com/Mohak-CODING-HEAVEN/VisionX/issues",
        "Changelog": "https://www.github.com/Mohak-CODING-HEAVEN/VisionX/releases"
    }
)
