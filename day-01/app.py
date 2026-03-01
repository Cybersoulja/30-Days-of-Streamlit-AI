import streamlit as st
import anthropic
import os
import html

st.set_page_config(page_title="Day 1 Review", page_icon="📝")

st.title("Day 1 Review - 30 Days of Streamlit")

def escape_markdown(text):
    """Utility function to escape markdown to prevent injection vulnerabilities."""
    return html.escape(text)

st.write("Reviewing Day 1 of the original 30 Days of Streamlit repository.")

day1_content = """# Setting up a local development environment

Before we can actually start building Streamlit apps, we will first have to setup a development environment.

Let's start by installing and setting up a conda environment.

## **Install conda**
- Install `conda` by going to https://docs.conda.io/en/latest/miniconda.html and choose your operating system (Windows, Mac or Linux).
- Download and run the installer to install `conda`.

## **Create a new conda environment**
Now that you have conda installed, let's create a conda environment for managing all the Python library dependencies.

To create a new environment with Python 3.9, enter the following:
```bash
conda create -n stenv python=3.9
```

where `create -n stenv` will create a conda environment named `stenv` and `python=3.9` will setup the conda environment with Python version 3.9.

## **Activate the conda environment**

To use a conda environment that we had just created that is named `stenv`, enter the following into the command line:

```bash
conda activate stenv
```

## **Install the Streamlit library**

It's now time to install the `streamlit` library:
```bash
pip install streamlit
```

## **Launching the Streamlit demo app**
To launch the Streamlit demo app (Figure 1) type:
```bash
streamlit hello
```"""

st.subheader("Original Content")
with st.expander("Show Day 1 Content"):
    st.markdown(escape_markdown(day1_content))

api_key = os.environ.get("ANTHROPIC_API_KEY")

if not api_key:
    st.warning("Please set the `ANTHROPIC_API_KEY` environment variable to run the AI review.")
else:
    if st.button("Generate AI Review"):
        with st.spinner("Generating review with Claude..."):
            try:
                client = anthropic.Anthropic(api_key=api_key)
                response = client.messages.create(
                    model="claude-3-opus-20240229",
                    max_tokens=1024,
                    messages=[
                        {"role": "user", "content": f"Please provide a helpful, constructive review of the following tutorial content for Day 1 of learning Streamlit:\n\n{day1_content}"}
                    ]
                )

                review = response.content[0].text
                st.subheader("AI Review")
                st.markdown(review)
            except Exception as e:
                st.error(f"Error generating review: {e}")
