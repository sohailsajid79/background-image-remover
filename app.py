import os
import zipfile
from flask import Flask, render_template, request, send_file
from rembg import remove
from threading import Thread

app = Flask(__name__)

def run_flask():
    app.run(debug=True)

# Route for the index page
@app.route('/')
def index():
    return (render_template('index.html'))

# Route for processing images
@app.route('/process', methods=['POST'])
def process_images():
    temp_dir = 'temp_images'
    os.makedirs(temp_dir, exist_ok=True)  # Create a temporary directory
    
    # Get list of files uploaded with the name 'image' from the request
    files = request.files.getlist('image')
    
    # Loop through each file
    for file in files:
        img_data = file.read()  # Read the file data
        output_data = remove(img_data)  # Process the image data to remove background
        filename = file.filename  # Get the filename
        
        output_path = os.path.join(temp_dir, filename)  # Create path for the output file
        
        # Write the processed image data to a file
        with open(output_path, 'wb') as o:
            o.write(output_data)
        
    zip_path = 'processed_images.zip'  # Path for the zip file
    
    # Create a zip file containing the processed images
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, file)
    
    # Remove the temporary files and directory
    for root, _, files in os.walk(temp_dir):
        for file in files:
            os.remove(os.path.join(root, file))
    os.rmdir(temp_dir)
      
    # Send the zip file as an attachment for download
    def start_server():
        app_thread = Thread(target=run_flask)
        app_thread.start()
    
    start_server()  # Start the server in a separate thread
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode if executed directly
