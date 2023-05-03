# Slack-Notification-AWS-CICD
Slack Pipeline Notifications
Slack Pipeline Notifications is a tool that sends notifications to developers through Slack messages when AWS CodePipeline fails. Instead of going to the AWS console to check the status of the pipeline, developers can receive a notification in real-time with the stage at which the pipeline failed, the execution ID, and the reason for the failure.

This project was developed as part of an internship with the objective of improving the developer experience with AWS CodePipeline. By providing immediate and actionable feedback, developers can address issues in the pipeline faster, reducing downtime and increasing productivity.

How it works
Slack Pipeline Notifications is a Python script that runs as an AWS Lambda function triggered by an AWS CloudWatch Event when a pipeline execution state changes to FAILED. The Lambda function sends a notification to a Slack channel with the details of the pipeline failure.

To use Slack Pipeline Notifications, you need to have an AWS account, a Slack workspace, and the necessary permissions to create an AWS Lambda function and a CloudWatch Event rule. The script can be configured with environment variables to customize the Slack channel, the Slack bot token, and the AWS region and pipeline name to monitor.

Installation and usage
Slack Pipeline Notifications is available on GitHub under an open-source license. To install and use the script, follow these steps:

Clone the repository: git clone https://github.com/<your_username>/slack-pipeline-notifications.git
Install the dependencies: pip install -r requirements.txt
Configure the environment variables: Copy the env.sample file to .env and update the values with your Slack and AWS credentials and pipeline configuration.
Deploy the Lambda function to AWS: serverless deploy
Test the notification: Trigger a pipeline failure and verify that a Slack message is sent to the configured channel.
The repository includes a README file with detailed instructions on how to set up Slack Pipeline Notifications step-by-step.

Contributions and feedback
Slack Pipeline Notifications is a community-driven project that welcomes contributions, feedback, and bug reports. If you have an idea for a new feature or improvement, feel free to open an issue or a pull request. If you encounter a problem with the script, please provide as much information as possible to help us reproduce and fix it.

By working together, we can make AWS CodePipeline and Slack integration more efficient and reliable for developers. Thank you for your interest in Slack Pipeline Notifications!
