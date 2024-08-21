# BotoDash

**BotoDash** is a web application designed to monitor and manage AWS resources using Flask and Boto3. It provides an intuitive dashboard for tracking EC2 instances and EBS volumes, offering real-time insights and easy management.

 ![image](https://github.com/user-attachments/assets/25fb5209-5602-42e8-a80c-37bcfe730eae)

## Features

- **Real-Time Monitoring**: View up-to-date information on your AWS EC2 instances and EBS volumes.
- **Interactive Dashboard**: Easily sort and view details with a user-friendly interface.
- **Comprehensive Insights**: Track instance types, states, public IP addresses, launch times, and volume sizes.

## Installation

### Prerequisites

- Python 3.6 or higher
- Flask
- Boto3
- AWS CLI

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/abisecops/botodash.git
   cd botodash
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Install and Configure AWS CLI:**

   - **Install AWS CLI**:
     
     Follow the instructions for your operating system:
     - [Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)
     - [macOS](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html)
     - [Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)

   - **Configure AWS CLI**:

     Run the following command and follow the prompts to set up your AWS credentials:

     ```bash
     aws configure
     ```

     You will need your AWS Access Key ID, Secret Access Key, default region name, and default output format.

6. **Set Up IAM Permissions:**

   - Create an IAM user or role with the necessary permissions to access EC2 and EBS resources. Ensure the user or role has the following permissions:
     - `ec2:DescribeInstances`
     - `ec2:DescribeVolumes`
   
   - Attach the IAM policy to your user or role that grants these permissions.

7. **Run the Application:**

   ```bash
   python app.py
   ```

   The application will start and be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the homepage to view and manage your EC2 instances and EBS volumes.
- Use the sortable table headers to organize and filter data as needed.

## Configuration

You can adjust application settings and AWS resource filters directly in the `app.py` file to fit your needs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to help improve BotoDash.

## Contact

For any questions or support, reach out via [Telegram](https://t.me/abis3c).
