# Background Removal Web App

This is a Flask web application that allows users to upload images (.jpg, .png) and remove the background using the rembg library. The processed images are then zipped and made available for download.

## Getting Started

To run this application locally, follow these steps:

1. Clone this repository to your local machine:
2. Install the required dependencies: pip3 install -r requirements.txt
3. Run the Flask application: python3 app.py
4. Open a web browser and navigate to `http://localhost:5000` to access the application.

## UI Diagram

![ui_app](./assets/UI.png)

## Usage

1. Click on the "Choose File" button to upload an image file (supported formats: .jpg, .png).
2. Click on the "Submit" button to process the uploaded image and remove its background.
3. Once processing is complete, the processed images will be available for download as a zip file.

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

![rembg](https://img.shields.io/badge/rembg-000000?style=for-the-badge&logo=python&logoColor=white)

![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)

![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## Acknowledgments

Special thanks to the creators of the rembg library for providing the background removal functionality and Coding Shiksha for the coding tutorial.