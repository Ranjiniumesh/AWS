import requests
import zipfile

source_url="https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.zip"
file_path="/home/ubuntu/Python/tomcat.zip"

def download_file(url, file_path):
    try:
        response = requests.get(url)
        with open(file_path, 'wb') as rs:
            rs.write(response.content)
            print ("File downloaded")
        with zipfile.ZipFile(file_path, 'r') as rs:
            rs.extractall("/home/ubuntu/Python")
            print("the zip file extracted")
    except requests.exceptions.RequestException as aa:
        print(f"Failed to download zip file")

download_file(source_url, file_path)
