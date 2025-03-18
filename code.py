import re
import json

def extract_name(text):
    """Extracts name by assuming the first capitalized words are the name."""
    name_match = re.findall(r'^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*', text, re.MULTILINE)
    return name_match[0] if name_match else "Not Found"

def extract_phone(text):
    """Extracts phone numbers in various formats."""
    phone_match = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return phone_match[0] if phone_match else "Not Found"

def extract_email(text):
    """Extracts email addresses."""
    email_match = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return email_match[0] if email_match else "Not Found"

def extract_skills(text):
    """Extracts skills from predefined skill set."""
    skills_list = {"Python", "Java", "SQL", "Machine Learning", "Data Analysis", "Excel", "Power BI", "C++", "JavaScript"}
    found_skills = [skill for skill in skills_list if re.search(rf'\b{skill}\b', text, re.IGNORECASE)]
    return found_skills if found_skills else "Not Found"

def extract_education(text):
    """Extracts education details like degree and university."""
    education_match = re.findall(r'\b(Bachelor|Master|PhD)[^,]+,\s[A-Za-z\s]+', text)
    return education_match if education_match else "Not Found"

def parse_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    parsed_data = {
        "Name": extract_name(text),
        "Phone": extract_phone(text),
        "Email": extract_email(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text)
    }
    
    return parsed_data

# Example usage
resume_path = "sample_resume.txt"  # Provide path to your text resume
parsed_resume = parse_resume(resume_path)

# Output results in JSON format
print(json.dumps(parsed_resume, indent=4))
