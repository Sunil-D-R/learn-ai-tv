import os
import yaml
import frontmatter
from pathlib import Path

# Category keywords mapping
CATEGORY_KEYWORDS = {
    "AI Agents": [
        "agent", "autonomous", "agentic", "cursor agent", "pydantic ai", 
        "ai assistant", "ai clone", "agent builder"
    ],
    "Development": [
        "api", "integration", "python", "code", "development", "full-stack",
        "implementation", "database", "next.js", "programming"
    ],
    "Prompt Engineering": [
        "prompt", "llm chain", "system prompt", "prompt engineering",
        "structured output", "prompt optimization"
    ],
    "RAG & Knowledge Management": [
        "rag", "retrieval", "vector", "embedding", "knowledge base",
        "pinecone", "supabase", "memor rag", "document"
    ],
    "Automation & Workflows": [
        "automation", "workflow", "no-code", "n8n", "make.com",
        "automate", "flow", "pipeline"
    ],
    "Content Generation & Marketing": [
        "content", "marketing", "seo", "video", "social media",
        "generate", "creation", "youtube"
    ]
}

def determine_categories(content, title, description):
    """Determine categories based on content analysis."""
    categories = set()
    
    # Convert all text to lowercase for case-insensitive matching
    text = f"{title} {description} {content}".lower()
    
    # Check for keywords in the text
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword.lower() in text for keyword in keywords):
            categories.add(category)
    
    # Ensure at least one category is assigned
    if not categories:
        # Default to "Development" if no clear category is found
        categories.add("Development")
    
    return sorted(list(categories))

def update_course_categories(courses_dir):
    """Update categories in course markdown files."""
    courses_path = Path(courses_dir)
    updated_count = 0
    
    for course_file in courses_path.glob("*.md"):
        try:
            # Read the current frontmatter
            post = frontmatter.load(course_file)
            
            # Get content for analysis
            content = post.content.lower()
            title = post.get('title', '').lower()
            description = post.get('description', '').lower()
            
            # Determine new categories
            new_categories = determine_categories(content, title, description)
            
            # Update categories if they've changed
            if set(new_categories) != set(post.get('categories', [])):
                post['categories'] = new_categories
                updated_count += 1
                
                # Write back to file
                with open(course_file, 'wb') as f:
                    frontmatter.dump(post, f)
                print(f"Updated categories for {course_file.name}")
                print(f"New categories: {new_categories}")
                print("---")
        except Exception as e:
            print(f"Error processing {course_file.name}: {str(e)}")
            continue
    
    return updated_count

if __name__ == "__main__":
    courses_dir = "/Users/air-sr/Library/CloudStorage/GoogleDrive-sunil@axysanalytics.com/My Drive/Learn AI TV/content/courses"
    total_updated = update_course_categories(courses_dir)
    print(f"\nTotal files updated: {total_updated}")
