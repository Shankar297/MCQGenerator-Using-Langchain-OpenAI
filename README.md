# MCQGenerator-Using-Langchain-OpenAI

# Streamlit Application Setup on AWS EC2

This guide will help you set up an Ubuntu EC2 instance on AWS and configure it to run a Streamlit application.

## Prerequisites
- An AWS account
- SSH client (like Terminal for macOS/Linux or PuTTY for Windows)
- Your repository URL

## Step 1: Log in to the AWS Management Console
1. Go to [AWS Management Console](https://aws.amazon.com/console/).
2. Enter your credentials to log in.

## Step 2: Launch an EC2 Instance
1. In the AWS Management Console, search for **EC2** in the search bar and click on **EC2**.
2. Click on the **Launch Instance** button.
3. Configure your instance:
    - **Name and tags:** Give your instance a name.
    - **Application and OS Images (Amazon Machine Image):** Select **Ubuntu Server 20.04 LTS (HVM), SSD Volume Type**.
    - **Instance type:** Select **t2.micro** (Free Tier eligible).
    - **Key pair (login):** Create a new key pair or select an existing one.
    - **Network settings:** Configure your VPC, subnet, and ensure that SSH access is allowed from your IP.
    - **Configure storage:** Default settings should suffice, or adjust according to your needs.
4. Click on **Launch Instance**.

## Step 3: Connect to Your EC2 Instance
1. Once the instance is running, select it and click on **Connect**.
2. Follow the instructions to SSH into your instance. Usually, the command looks like this:
    ```sh
    ssh -i "your-key-pair.pem" ubuntu@your-ec2-public-dns
    ```

## Step 4: Update and Install Required Packages
1. Update your package lists and upgrade the system:
    ```sh
    sudo apt update
    sudo apt-get update
    sudo apt upgrade -y
    ```

2. Install essential packages:
    ```sh
    sudo apt install git curl unzip tar make sudo vim wget -y
    ```

## Step 5: Clone Your Repository
1. Clone your Git repository:
    ```sh
    git clone "Your-repository"
    ```
   Replace `"Your-repository"` with the URL of your Git repository.

## Step 6: Install Python and Streamlit Requirements
1. Install Python 3 and pip:
    ```sh
    sudo apt install python3-pip -y
    ```

2. Navigate to your cloned repository directory:
    ```sh
    cd your-repository-directory
    ```

3. Install the required Python packages:
    ```sh
    pip3 install -r requirements.txt
    ```

## Step 7: Run Your Streamlit Application
1. Run the Streamlit application:
    ```sh
    python3 -m streamlit run StreamlitAPP.py
    ```

## Step 8: (Optional) Add OpenAI API Key
1. Create a `.env` file in your server:
    ```sh
    touch .env
    vi .env
    ```
2. Press `i` to enter insert mode and add your OpenAI API key:
    ```
    OPENAI_API_KEY="***********************************88"
    ```
3. Save and exit:
    - Press `Esc`, then type `:wq`, and hit `Enter`.

## Step 9: Configure Security Group to Allow Streamlit Port
1. Go to the EC2 Dashboard.
2. Select your instance and click on the **Security** tab.
3. Click on the security group link associated with your instance.
4. Click on **Edit inbound rules**.
5. Add a new rule to allow traffic on port 8501:
    - Type: Custom TCP
    - Port range: 8501
    - Source: Anywhere (0.0.0.0/0) or My IP

## Step 10: Access Your Streamlit App
1. Open your web browser and go to:
    ```
    http://your-ec2-public-dns:8501
    ```
   Replace `your-ec2-public-dns` with your EC2 instance's public DNS name.

Your Streamlit application should now be up and running!
