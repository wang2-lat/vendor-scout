# Vendor Scout

CLI tool to find and evaluate reliable outsourcing vendors for startups.

## Problem It Solves

Startups struggle with:
- Finding trustworthy outsourcing vendors (especially for AI projects)
- Avoiding vendors who only build demos, not production-ready products
- Evaluating vendors based on real project history
- Creating clear requirement documents to communicate with vendors

## Installation


## Usage

### Search for vendors

### View vendor details

### Generate requirement document template

## Features

- **Smart Search**: Filter vendors by skills, rating, and project count
- **Detailed Profiles**: View vendor history, reviews, and specializations
- **Requirement Templates**: Generate standardized project documents to avoid miscommunication

## Tips for Choosing Vendors

1. Look for vendors with 4.5+ rating and 30+ completed projects
2. Check if they have experience in your specific domain (AI, Web, Mobile)
3. Read reviews carefully - look for mentions of "production-ready" and "scalable"
4. Use the requirement template to clearly communicate your needs
5. Ask for references and previous work samples

## Example Workflow

# 安装
pip install -r requirements.txt

# 搜索 AI 领域高评分服务商
python main.py search --skill AI --min-rating 4.5

# 查看详情
python main.py detail 1

# 生成需求文档
python main.py template --output my-ai-project.md --project-type AI