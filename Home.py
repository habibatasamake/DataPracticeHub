import streamlit as st
from utils import load_projects

# Charger les projets depuis le répertoire 'projects'
projects = load_projects()

# Configuration de la page
st.set_page_config(
    page_title="DataPracticeHub",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Titre de la page
st.title("DataPracticeHub")

# Sidebar pour la navigation
st.sidebar.title("Navigation")
pages = ["Accueil", "Projets", "À propos"]
page = st.sidebar.radio("Aller à", pages)

# Fonction pour afficher les détails d'un projet
def show_project_details(project_name):
    project = projects[project_name]
    st.header(project_name)
    st.write(project["description"])
    st.image(project["image"])
    st.write("### Instructions")
    for instruction in project["instructions"]:
        st.write(instruction)
    st.write("### Ressources")
    for resource in project["resources"]:
        st.write(resource)

if page == "Accueil":
    st.header("Bienvenue sur DataPracticeHub")
    st.write("DataPracticeHub est un répertoire de projets réels en Data Science pour vous aider à apprendre par la pratique.")
    st.write("Choisissez un projet ci-dessous pour commencer :")

    # Exemples de projets sur la page d'accueil
    cols = st.columns(3)

    for i, (project_name, project) in enumerate(projects.items()):
        with cols[i % 3]:
            st.subheader(project_name)
            st.image(project["image"])
            st.write(project["description"])
            if st.button("Détails", key=project_name):
                st.session_state.page = project_name

elif page == "Projets":
    st.header("Tous les Projets")
    st.write("Liste de tous les projets disponibles :")

    # Liste des projets
    for project_name, project in projects.items():
        st.subheader(project_name)
        st.write(project["description"])
        if st.button("Détails", key=project_name):
            st.session_state.page = project_name

elif page == "À propos":
    st.header("À propos de DataPracticeHub")
    st.write("DataPracticeHub est conçu pour aider les passionnés de Data Science à apprendre en réalisant des projets pratiques.")
    st.write("Pour toute question, contactez-nous à [votre-email@example.com](mailto:votre-email@example.com)")

# Détail du projet (logique simplifiée)
if "page" in st.session_state and st.session_state.page in projects:
    show_project_details(st.session_state.page)