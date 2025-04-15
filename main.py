import subprocess
import os
import sys

def main():
    """
    Main entry point for the Face Recognition application.
    This function ensures the application uses the dlib_env environment
    and handles any errors that might occur.
    """
    print("Face Recognition System")
    print("----------------------")
    
    # Get the current Python interpreter path
    current_python = sys.executable
    print(f"Current Python interpreter: {current_python}")
    
    # Define the path to the dlib_env Python interpreter
    dlib_env_python = r"C:\Users\grizi\dlib_env\Scripts\python.exe"
    
    # Check if the script to run exists
    script_to_run = "facerecog.py"
    if not os.path.exists(script_to_run):
        print(f"Error: Could not find the script {script_to_run}")
        sys.exit(1)
    
    # Run the facerecog.py script using the dlib_env interpreter
    try:
        print(f"Running with interpreter: {dlib_env_python}")
        subprocess.run([dlib_env_python, script_to_run], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_to_run}: {e}")
    except FileNotFoundError:
        print(f"Error: Could not find the Python interpreter at {dlib_env_python}")
        print("Please make sure the dlib_env environment exists at the specified path.")

if __name__ == "__main__":
    main() 