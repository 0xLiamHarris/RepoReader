# main.py
import os
import tempfile
from dotenv import load_dotenv
from config import WHITE, GREEN, RESET_COLOR
from file_processing import clone_github_repo, load_and_index_files
from questions import ask_question

load_dotenv()

def main():
    github_url = input("Enter the GitHub URL of the repository: ")
    repo_name = github_url.split("/")[-1]
    print("Cloning the repository...")
    
    with tempfile.TemporaryDirectory() as local_path:
        if clone_github_repo(github_url, local_path):
            index, documents, _, _ = load_and_index_files(local_path)
            if index is None:
                print("No documents were found to index. Exiting.")
                return

            print("Repository cloned. Indexing files...")
            
            while True:
                user_question = input("\n" + WHITE + "Ask a question about the repository (type 'exit()' to quit): " + RESET_COLOR)
                if user_question.lower() == "exit()":
                    break

                print('Thinking...')
                answer = ask_question(user_question, repo_name, github_url)
                print(GREEN + '\nANSWER\n' + answer + RESET_COLOR + '\n')

        else:
            print("Failed to clone the repository.")

if __name__ == "__main__":
    main()
