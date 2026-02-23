import streamlit as st
import agentops
import os
import sys
from dotenv import load_dotenv

# Add src to sys.path to allow importing the content_router package
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from content_router.flow import ContentRouterFlow

# 🎨 Streamlit Page Configuration
st.set_page_config(
    page_title="Content Router Studio",
    page_icon="🚀",
    layout="wide",
)

# 🧠 Initialize Observability
load_dotenv()
agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))

def main():
    st.title("🚀 Content Router Studio")
    st.markdown("""
    Transform any web content into high-quality **Blog Posts**, **Newsletters**, or **LinkedIn Posts** using specialized AI crews.
    """)

    # 🛠️ Sidebar Configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        url = st.text_input("🔗 Source URL", placeholder="https://blog.crewai.com/...")
        content_type = st.selectbox(
            "📝 Target Content Type",
            options=["blog", "newsletter", "linkedin"],
            format_func=lambda x: x.capitalize()
        )
        
        kickoff_btn = st.button("⚡ Run Flow", type="primary", use_container_width=True)

    # 📊 Main Content Area
    if kickoff_btn:
        if not url:
            st.error("Please provide a valid URL.")
            return

        with st.status("🧠 Flow in progress...", expanded=True) as status:
            st.write("Initializing flow state...")
            flow = ContentRouterFlow()
            flow.state.url = url
            flow.state.content_type = content_type
            
            st.write(f"Routing to {content_type.capitalize()} crew...")
            try:
                flow.kickoff()
                
                if flow.state.error:
                    status.update(label="❌ Flow Execution Failed", state="error", expanded=True)
                    st.error(flow.state.error)
                else:
                    status.update(label="✅ Flow Execution Complete", state="complete", expanded=False)
                    
                    st.divider()
                    st.subheader(f"📝 Generated {content_type.capitalize()} Content")
                    st.markdown(flow.state.final_content)
                    
                    with st.expander("🔍 View Flow Metadata"):
                        st.json({
                            "url": flow.state.url,
                            "content_type": flow.state.content_type,
                            "content_length": len(flow.state.final_content)
                        })
            except Exception as e:
                status.update(label="💥 Unexpected Error", state="error", expanded=True)
                st.error(f"An unexpected error occurred: {str(e)}")

    else:
        # Initial Landing State
        st.info("Enter a URL and select a content type in the sidebar to get started.")
        
        # Display Architecture Diagram
        with st.expander("🏗️ View System Architecture"):
            st.markdown("""
            ```mermaid
            graph TD
                A[User Input] --> B[ContentRouterFlow]
                B --> C{Router}
                C -- blog --> D[Blog Crew]
                C -- newsletter --> E[Newsletter Crew]
                C -- linkedin --> F[LinkedIn Crew]
                D & E & F --> G[Final Content]
            ```
            """)

if __name__ == "__main__":
    main()
