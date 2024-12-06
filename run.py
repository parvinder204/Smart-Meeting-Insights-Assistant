import subprocess
import os
import sys

# Function to run the Django server
def run_django():
    print("Starting the Django development server...")
    django_command = ["python", "backend/manage.py", "runserver"]
    subprocess.run(django_command)

# Function to run the Next.js server
def run_nextjs():
    print("Starting the Next.js development server...")
    # Set the environment variable for the Next.js server
    os.environ['NEXT_PUBLIC_API_URL'] = 'http://localhost:8000/api'
    subprocess.run(["npm", "run", "dev"], cwd="frontend")

def main():
    # Start both servers concurrently using subprocess
    print("Starting the project...")
    try:
        # Run Django server in the background
        django_process = subprocess.Popen(run_django)
        # Run Next.js server
        run_nextjs()
    except KeyboardInterrupt:
        print("\nShutting down the servers...")
        # Gracefully terminate both processes if CTRL+C is pressed
        django_process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
