import requests
import tarfile

source_url="https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz"
file_path="/home/ubuntu/Python/Tomcat.tar.gz"

def download_file(url, file_path):
    try:
        response = requests.get(url)
        with open(file_path, 'wb') as rs:
            rs.write(response.content)
            print ("File downloaded")
        with tarfile.open(file_path, 'r') as rs:
            rs.extractall("/home/ubuntu")
            print("the file extracted")
    except requests.exceptions.RequestException as aa:
        print(f"Failed to download")

download_file(source_url, file_path)  
