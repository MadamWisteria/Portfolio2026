# Portfolio2026
Serverless Cloud Resume & Visitor Counter
A high-performance, responsive portfolio website hosted on AWS using a completely serverless architecture. This project demonstrates full-stack cloud integration, featuring a live visitor counter powered by Python, Lambda, and DynamoDB.

🚀 Live Demo
[d2bozrp3q7x45i.cloudfront.net](url)

🏗️ The Architecture
The project follows a "Decoupled" architecture to ensure speed, security, and scalability:

Frontend: HTML & CSS hosted in an Amazon S3 bucket.

Content Delivery: Amazon CloudFront for global distribution and HTTPS encryption.

API Layer: AWS Lambda (Python 3.12) providing a serverless backend.

Database: Amazon DynamoDB for persistent, atomic visitor count tracking.

Security: CORS-enabled headers and IAM roles following the principle of least privilege.

🛠️ Technical Breakdown
1. Python Backend (Lambda)
The core logic is written in Python using the boto3 library. It performs an atomic update on the DynamoDB table to ensure the counter increments correctly even if multiple people visit the site simultaneously.

2. Frontend Integration (JavaScript)
The frontend uses the Asynchronous Fetch API to communicate with the AWS Lambda Function URL. It gracefully handles the data exchange and updates the DOM without requiring a page refresh.

3. Infrastructure as Code (Concept)
The site is optimised for global performance using CloudFront's edge locations, significantly reducing latency for users worldwide.

💻 Skills Demonstrated
Cloud Platforms: AWS (S3, CloudFront, Lambda, DynamoDB, IAM).

Programming: Python, JavaScript, HTML, CSS.

👤 Contact
Kiara Tshabalala * Email: kiaratshabalala12@gmail.com
