![BMW_Logo](https://github.com/NTUST-BMW-Lab/ips-crawler-aruba/assets/88525718/5028a5a5-6372-4106-aef9-e823f7db1222)

#  Aruba AP Indoor Positioning Crawling
###### tags: `WiFi`

Made By : Dio (@IdleGoat) and Daniel (@danielandrewr)
## Table of Contents
- [Aruba AP Indoor Positioning Crawling](#aruba-ap-indoor-positioning-crawling)
          - [tags: `WiFi`](#tags-wifi)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Description](#description)
    - [](#)
  - [Installation](#installation)
    - [Mongo DB Installation](#mongo-db-installation)
      - [Installing MongoDB](#installing-mongodb)
      - [Set Up Static Ip Configuration](#set-up-static-ip-configuration)
      - [How to do set up connection to MongoDB](#how-to-do-set-up-connection-to-mongodb)
    - [Conda Installation](#conda-installation)
    - [Setting up the Conda Environment](#setting-up-the-conda-environment)
    - [Creating Environment Variables with a `.env` File](#creating-environment-variables-with-a-env-file)
    - [Running the Code](#running-the-code)
  - [Progress Log](#progress-log)
      - [2023/07/18](#20230718)
      - [2023/07/20](#20230720)
  - [References](#references)
## Introduction
### Description
The Aruba AP-Indoor Crawling Code is a Python-based project that enables crawling and data extraction specifically from indoor access points (APs) managed by Aruba controllers. The code utilizes Aruba APIs  to gather information such as MAC addresses, signal strength, and other relevant data from the APs for Indoor positioning purposes.

### How The Crawler Works

### Data Fields Description

1. **Ap-Type**
   - Shows classification of the AP (Access Point).

2. **Curr-rssi**
   - Current Received Signal Strength Indication (RSSI).
   - RSSI is a measure of the signal strength at the receiver, indicating the power level of the received signal.

3. **Band**
   - The frequency range used by the AP (e.g., 2.4 GHz or 5 GHz).
   - Specifies the wireless frequency at which the AP operates.

4. **Channel**
   - A specific frequency used for transmitting and receiving data by the AP.
   - Indicates the channel number or frequency band the AP is using.

5. **Timestamp**
   - The date and time when the information was recorded.
   - Provides the exact time when the data was collected.

6. **Essid**
   - Extended Service Set Identifier (ESSID).
   - ESSID is a unique name identifier assigned to the wireless network or AP.

7. **EIRP**
   - Equivalent Isotropically Radiated Power (EIRP).
   - EIRP represents the amount of power emitted by a wireless device, including both the transmitter power and antenna gain.

8. **Ap-Name**
   - The Name Of The AP retrieving the data.
   - Refers to the specific name or identifier of the Access Point.

9. **Bssid**
   - Basic Service Set Identifier (BSSID).
   - BSSID is a unique identifier assigned to the wireless access point, used to distinguish it from other APs in the area.

## Installation
### Mongo DB Installation

#### Installing MongoDB
1. Visit the MongoDB download page at https://www.mongodb.com/try/download/community.
![](https://hackmd.io/_uploads/ByUJ3baF2.png)
2. Under the "Community Server" tab, click on the "Download" button for the latest version of MongoDB.

3. Once the download is complete, locate the installer file and double-click on it.

4. Follow the instructions in the installer, including selecting the components you want to install and the installation directory.

5. After the installation is complete, MongoDB will be ready to use.
#### Set Up Static Ip Configuration
1. Open the MongoDB configuration file (mongod.conf) using a text editor. The location of this file depends on your operating system and installation method. C:\Program Files\MongoDB\Server\{version}\bin\mongod.cfg on Windows.

    ![](https://hackmd.io/_uploads/rytvpxxY2.png)

2. Look for the bindIp setting in the configuration file. By default, it is set to 127.0.0.1, which binds MongoDB to the localhost only. Change the ip to your static IP
    ```
    bindIp: 127.0.0.1, 192.168.0.100
    ```
    and then save the file and restart the mongodb services 

3. Then create Firewall rules to allow connection to the mongodb port. Open Advanced security in Windows Defender and then click inbound rules
    ![](https://hackmd.io/_uploads/ryWYyWlth.png)

4. Create new rules to allow connection to port 27017
    ![](https://hackmd.io/_uploads/HysbxbeYn.png)
    and don't forget to allow the connection

#### How to do set up connection to MongoDB
1. **Using MongoDB Compass**
    put the connection string inside 
    
    ```
    mongodb://<static ip address>:27017
    ```
    
    ![](https://hackmd.io/_uploads/r1v0O-eth.jpg)
    
2. **Using MongoDB Shell**

    Install MongoDB shell from [here](https://www.mongodb.com/try/download/shell)
    use this connection string
    
    ```
    mongosh mongodb://<static ip>:27017/
    ```
    ![](https://hackmd.io/_uploads/rJZDh-xFh.jpg)


### Conda Installation

1. Install Conda: Conda is a package management system that allows you to create and manage isolated environments for your Python projects. Follow these steps to install Conda:

   - Visit the [Conda](https://docs.conda.io/en/latest/) website and download the appropriate installer for your operating system
- Run the installer and follow the instructions to complete the installation.

2. Ensure Conda is added to the system's PATH: After installing Conda, you need to make sure it is added to the system's PATH environment variable. This ensures that the `conda` command is recognized and can be executed from any location in the terminal or command prompt.

   - **Windows**

     by default, Conda should add itself to the PATH during installation. However, if you encounter issues, you can manually add it to the PATH by following these steps:

     ​	2.1 Open the Start menu and search for "Environment Variables".

     ​	2.2 Click on "Edit the system environment variables".

     ​	2.3 In the "System Properties" window, click on the "Environment Variables" button.

     ​	2.4 In the "System Variables" section, scroll down and locate the "Path" variable.

     ​	2.5 Click on "Edit" and add the path to the Conda installation directory (e.g., `	C:\Users\YourUsername\anaconda3\`) at the end of the existing values, separating it with a semicolon

     ​	2.6 Click "OK" to save the changes.

   - **macOS and Linux**

     Conda should automatically add itself to the PATH during installation. 

     

   To verify, open a new terminal or command prompt and run the following command. If the command displays the Conda version without any errors, it means Conda is correctly added to the PATH.

   ```shell
   conda --version
   ```

   

### Setting up the Conda Environment 

1. Create the Conda environment: Once Conda is installed, you can create a new environment for your project. Open a terminal or command prompt and run the following command:
  ```shell
  conda env create --file environment.yml
  ```

  This command will create a new Conda environment using the specifications defined in the `environment.yml` file. Make sure the `environment.yml` file is located in the current directory or provide the full path to the file.

2. Activate the Conda environment: To activate the environment, run the appropriate command based on your operating system:

  - **Windows**

    ```shell
    conda activate Crawler_Fix
    ```

  - **macOS and Linux**

    ```shell
    source activate Crawler_Fix
    ```

    

### Creating Environment Variables with a `.env` File

1. Create a new file in your project directory and name it `.env`. The leading dot is important as it indicates that the file should be treated as a hidden file.

2. Open the `.env` file in a text editor and define your environment variables using the `KEY=VALUE` format. For example:

   ```
   ARUBA_USERNAME="test"
   ARUBA_PASSWORD="test"
   ARUBA_IPADDRESS="192.168.291.1"
   MONGODB_URI = "mongodb://<MONGODB IP ADD>:27017/"
   MONGODB_NAME = "wifi_crawl"
   ```
The `.env` file contains the following environment variables that are used for the Aruba controller:

- `ARUBA_USERNAME`: The username used to log in to the Aruba controller.

- `ARUBA_PASSWORD`: The password associated with the Aruba controller account.

- `ARUBA_IPADDRESS`: The IP address of the Aruba controller.
   Add these environment variables, with each variable on a new line. Replace the values ("test",  "192.168.291.1") with the actual values you need.

- `MONGODB_URI`: The URI for connecting to your MongoDB database.

- `MONGODB_NAME`: The name of the MongoDB database where the crawled data will be stored.
  
3. Save the `.env` file.

4. The Env File should look like this

   ![](https://hackmd.io/_uploads/r1HzAc7Kh.png)

   

### Running the Code

1. Make sure the Conda environment is activated by running the appropriate command mentioned in the "Activate the Conda environment" section above.

2. Navigate to the directory containing your Python code:

   ```shell
   cd /path/to/your/code
   ```

3. Run the Python script

   ```shell
   python main.py
   ```



Make sure to replace `/path/to/your/code` with the actual path to your code directory, and modify any placeholder values (`environment.yml`, `myenv`, `MY_VARIABLE`, etc.) with the appropriate values based on your project.

Including the `environment.yml` file in the documentation allows others to recreate the same environment by following the provided instructions.



## Progress Log
#### 2023/07/18
Attending 6G Conference

<img src="https://github.com/NTUST-BMW-Lab/ips-crawler-aruba/assets/88525718/624071e5-19d2-4be8-8079-99f0d210755d" height="400">



#### 2023/07/20
Testing Crawling Code in D1

<img src="https://github.com/NTUST-BMW-Lab/ips-crawler-aruba/assets/88525718/07c3a399-1a87-437c-84d7-681da3a41505" height="400">


## References

