from typing import List, Optional
from models import Vendor, Review, SearchFilters

MOCK_VENDORS = [
    Vendor(
        id=1,
        name="AI Solutions Pro",
        skills=["AI", "Machine Learning", "NLP", "Computer Vision"],
        rating=4.8,
        completed_projects=45,
        price_range="$5000-$15000",
        location="San Francisco, USA",
        description="Specialized in production-ready AI solutions, not just demos. We focus on scalable ML systems that actually work in real business environments.",
        reviews=[
            Review(rating=5.0, project_type="AI Chatbot", comment="Delivered a production-ready chatbot that handles 10k+ daily users. Great communication."),
            Review(rating=4.5, project_type="ML Pipeline", comment="Solid work on our recommendation system. Minor delays but quality was excellent."),
        ]
    ),
    Vendor(
        id=2,
        name="WebCraft Studios",
        skills=["Web Development", "React", "Node.js", "AWS"],
        rating=4.6,
        completed_projects=120,
        price_range="$3000-$10000",
        location="Austin, USA",
        description="Full-stack web development with focus on modern frameworks and cloud deployment. We help startups launch fast.",
        reviews=[
            Review(rating=4.8, project_type="SaaS Platform", comment="Built our MVP in 6 weeks. Clean code and good documentation."),
            Review(rating=4.4, project_type="E-commerce Site", comment="Professional team, delivered on time and within budget."),
        ]
    ),
    Vendor(
        id=3,
        name="Mobile First Labs",
        skills=["Mobile Development", "iOS", "Android", "Flutter"],
        rating=4.7,
        completed_projects=80,
        price_range="$4000-$12000",
        location="London, UK",
        description="Cross-platform mobile apps that feel native. We specialize in consumer-facing apps with great UX.",
        reviews=[
            Review(rating=4.9, project_type="Fitness App", comment="Amazing UI/UX work. App got featured on App Store."),
            Review(rating=4.5, project_type="Social App", comment="Good technical skills, responsive to feedback."),
        ]
    ),
    Vendor(
        id=4,
        name="DataDrive Analytics",
        skills=["AI", "Data Science", "Python", "Analytics"],
        rating=4.5,
        completed_projects=35,
        price_range="$6000-$18000",
        location="Berlin, Germany",
        description="Turn your data into actionable insights. We build custom analytics dashboards and predictive models.",
        reviews=[
            Review(rating=4.6, project_type="Analytics Dashboard", comment="Great data visualization work. Helped us understand our customers better."),
        ]
    ),
    Vendor(
        id=5,
        name="CloudScale DevOps",
        skills=["DevOps", "AWS", "Kubernetes", "CI/CD"],
        rating=4.9,
        completed_projects=60,
        price_range="$4000-$14000",
        location="Singapore",
        description="Infrastructure automation and cloud optimization. We help startups scale without breaking the bank.",
        reviews=[
            Review(rating=5.0, project_type="AWS Migration", comment="Reduced our cloud costs by 40% while improving performance. Highly recommended."),
            Review(rating=4.8, project_type="CI/CD Pipeline", comment="Professional setup, great documentation for our team."),
        ]
    ),
]

def get_vendors(filters: SearchFilters) -> List[Vendor]:
    """Filter vendors based on search criteria"""
    results = MOCK_VENDORS.copy()
    
    if filters.skill:
        skill_lower = filters.skill.lower()
        results = [v for v in results if any(skill_lower in s.lower() for s in v.skills)]
    
    if filters.min_rating:
        results = [v for v in results if v.rating >= filters.min_rating]
    
    if filters.min_projects:
        results = [v for v in results if v.completed_projects >= filters.min_projects]
    
    return sorted(results, key=lambda x: x.rating, reverse=True)

def get_vendor_by_id(vendor_id: int) -> Optional[Vendor]:
    """Get vendor details by ID"""
    for vendor in MOCK_VENDORS:
        if vendor.id == vendor_id:
            return vendor
    return None

def generate_requirement_template(project_type: str) -> str:
    """Generate a project requirement document template"""
    template = f"""# Project Requirement Document

## Project Overview
**Project Type:** {project_type}
**Company Name:** [Your Company]
**Contact:** [Your Email]
**Budget Range:** $[Min] - $[Max]
**Timeline:** [Expected Duration]

## Business Context
**Problem Statement:**
[Describe the problem you're trying to solve]

**Target Users:**
[Who will use this product?]

**Success Metrics:**
[How will you measure success?]

## Technical Requirements

### Core Features
1. [Feature 1 - describe in detail]
2. [Feature 2 - describe in detail]
3. [Feature 3 - describe in detail]

### Technical Stack Preferences
- Backend: [e.g., Python, Node.js, or vendor's choice]
- Frontend: [e.g., React, Vue, or vendor's choice]
- Database: [e.g., PostgreSQL, MongoDB, or vendor's choice]
- Hosting: [e.g., AWS, GCP, or vendor's choice]

### Integration Requirements
- [List any third-party services to integrate]
- [API requirements]

## Non-Functional Requirements
- **Performance:** [e.g., handle 1000 concurrent users]
- **Security:** [e.g., GDPR compliance, data encryption]
- **Scalability:** [e.g., support 10x growth in 6 months]

## Deliverables
- [ ] Source code with documentation
- [ ] Deployment scripts
- [ ] User documentation
- [ ] Admin documentation
- [ ] Test coverage report

## Project Phases
**Phase 1 (Weeks 1-2):** [MVP features]
**Phase 2 (Weeks 3-4):** [Additional features]
**Phase 3 (Weeks 5-6):** [Polish and deployment]

## Communication & Collaboration
- **Preferred Communication:** [Slack, Email, etc.]
- **Meeting Frequency:** [Weekly, Bi-weekly]
- **Project Management:** [Jira, Trello, etc.]

## Red Flags to Avoid
- Vendors who promise unrealistic timelines
- No clear milestone-based payment structure
- Lack of previous production deployments
- Poor communication during initial discussions

## Questions for Vendors
1. Can you show similar projects you've completed?
2. What's your typical development process?
3. How do you handle scope changes?
4. What's included in post-launch support?
5. Can you provide references from previous clients?

---
**Note:** This is a living document. Update it as you refine your requirements.
"""
    return template
