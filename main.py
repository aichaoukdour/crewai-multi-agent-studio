import sys
import os

# Add src to sys.path to allow importing the content_router package
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from content_router.flow import ContentRouterFlow
import agentops
from dotenv import load_dotenv

load_dotenv()
agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))

def main():
    """Main entry point to run the Content Router Flow"""
    print("🚀 Initializing Content Router Flow...")
    flow = ContentRouterFlow()
    
    print("\n⚡ Running Flow...")
    flow.kickoff()
    
    print("\n" + "="*50)
    print("📊 FLOW EXECUTION COMPLETE")
    print("="*50)
    
    print("\n" + "-"*50)
    print("📝 Generated Content Snapshot")
    print("-" * 50)
    # Print the first 200 characters of the final content
    content = str(flow.state.final_content)
    if content:
        print(content[:200] + "..." if len(content) > 200 else content)
    else:
        print("No content generated.")
    print("-" * 50)
    
    print("\n🧠 Flow State Summary")
    print(f"URL: {flow.state.url}")
    print(f"Content Type: {flow.state.content_type}")
    print(f"Final Content Length: {len(content)} characters")
    if flow.state.error:
        print(f"⚠️ Error: {flow.state.error}")

if __name__ == "__main__":
    main()
