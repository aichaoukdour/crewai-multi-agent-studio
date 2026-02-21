from flow import ContentRouterFlow

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

if __name__ == "__main__":
    main()
