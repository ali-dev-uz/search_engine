# Google Custom Search API Integration

<br> This guide walks you through the steps to obtain and use the Google Custom Search API for your projects.<br>
---
## Step 1: Get Access to Google Custom Search API

### Create a Google Cloud Project:
-Go to the [Google Cloud Console](https://console.cloud.google.com/project).
-Click on the project dropdown and select "New Project."
-Name your project and click "Create."

### Enable the Custom Search API:
-In the Google Cloud Console, navigate to the API Library.
-Search for "Custom Search API" and select it.
-Click "Enable" to activate the API for your project.

### Generate an API Key:
-Go to the Credentials page.
-Click on "Create Credentials" and select "API Key."
-Copy the generated API key and store it securely; you will need it to authenticate your API requests.

---
## Step 2: Set Up a Custom Search Engine
### Create a Custom Search Engine:
-Visit the Custom Search Engine Control Panel.
-Click "Add" to create a new search engine.
-Enter the site(s) you want to search, or choose "Search the entire web" for broader search capabilities.
-After setup, note down the "Search Engine ID" (cx). You’ll need this ID for API requests.

### Configure Your Search Engine
-Customize your search engine settings to refine search results, set up filters, and adjust other preferences to meet your specific needs.
