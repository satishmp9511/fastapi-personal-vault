# fastapi-personal-vault
Simple FastAPI Authentication & File ManagerA lightweight web application built with FastAPI, SQLite, and Jinja2 Templates that handles user registration, authentication, and personalized text file management.🚀 FeaturesUser Authentication: Sign up and log in securely backed by SQLite (data.db).Personalized File Storage: Automatically generates an individual .txt note file for every newly registered user inside the all/ directory.Live Text Editor: Users can view, update, and save changes directly to their personal text files.Static Asset Support: Configured with FastAPI's StaticFiles for custom styling.🛠️ Project Structure.
├── all/                  # Stores individual user text files
├── style/                # Static stylesheets
├── template/             # Jinja2 HTML templates
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
├── .gitignore            # Ignored files for Git
└── README.md             # Documentation
⚙️ Installation & Running Locally1. Clone the Repositorygit clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
2. Create and Activate a Virtual Environment# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependenciespip install -r requirements.txt
4. Run the Applicationpython -m uvicorn main:app --reload
Open your browser and go to: http://127.0.0.1:8000📌 API EndpointsMethodEndpointDescriptionGET / POST/Home page / Login formPOST/loginValidates credentials and loads the user dashboardPOST/readUpdates and saves the user's personal text fileGET/goOpens the new account registration pagePOST/newRegisters a new user and creates their text file
