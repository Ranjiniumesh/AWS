from jfile import download_file

url="https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.18/bin/apache-tomcat-10.1.18.tar.gz"
filepath="/home/ubuntu/Tomcat10.tar.gz"

download_file(url, filepath)

