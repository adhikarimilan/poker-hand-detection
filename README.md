# Poker Hand Detection with YOLO and Python

This repository contains a real time computer vision system to detect playing cards and classify poker hands. You can use this tool to automate game analysis or identify hand rankings from video streams.

## Features

* Detects all 52 standard playing cards.
* Processes live webcam feeds or video files.
* Uses YOLO for high speed object detection.
* Includes custom logic to identify ten poker hand rankings.
* Provides visual overlays for detected cards and the final hand result.

## Technology Stack

* Python: Core programming language.
* YOLO (Ultralytics): Object detection model.
* OpenCV: Video processing and frame manipulation.
* CVZone: Visual overlays and text rendering.
* Roboflow: Source for the card dataset.
* Google Colab: Environment used for model training.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies:
   pip install numpy ultralytics cvzone opencv-python
3. Ensure you have the pokerhand.pt weight file in the weights directory.

## How It Works

The system follows a three step process:

1. Detection: The YOLO model identifies individual cards in the frame and provides bounding boxes.
2. Extraction: The script extracts the rank and suit from the detected class names.
3. Classification: The find_poker_hand function evaluates the unique combination of cards to determine the best possible hand, such as a Full House or Royal Flush.

## Usage

1. Place your video file in the resources/videos directory or uncomment the webcam code in the main script.
2. Run the main script:
   python main.py
3. Press the Esc key to exit the video stream.

## Poker Hand Logic

The system evaluates the following hands in descending order of rank:

* Royal Flush
* Straight Flush
* Four of a Kind
* Full House
* Flush
* Straight
* Three of a Kind
* Two Pair
* One Pair
* High Card
