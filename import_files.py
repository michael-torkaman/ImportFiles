import os
import sys
import subprocess

# run donnet add sln to command
def add_csproj_to_solution(solution_path, project_path):
    solution_filename = os.path.basename(solution_path)
    project_filename = os.path.basename(project_path)
    project_name = os.path.splitext(project_filename)[0]

    # check if files exisit
    if not os.path.isfile(solution_path):
        print(f"Error: Solution file '{solution_filename}' not found.")
        return

    if not os.path.isfile(project_path):
        print(f"Error: Project file '{project_filename}' not found.")
        return

    # Run the command to add the project to the solution
    try:
        subprocess.run(
            ["dotnet", "sln", solution_path, "add", project_path],
            # did it work
            check=True,
            text=True,
        )
        print(f"Added '{project_name}' to '{solution_filename}'")
        #errormeasage
    except subprocess.CalledProcessError as e:

        print(f"Error adding '{project_name}' to '{solution_filename}': {e}")



def find_and_add_csproj_files(solution_path, project_directory):
    for root, _, files in os.walk(project_directory):
        for filename in files:
            if filename.endswith(".csproj"):
                project_path = os.path.join(root, filename)
                add_csproj_to_solution(solution_path, project_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_project_to_solution.py <path to copy to> <path to copy from>")
        sys.exit(1)

    solution_path = sys.argv[1]
    project_directory = sys.argv[2]

    # Check if the project directory exists
    if not os.path.isdir(project_directory):
        print(f"Error: Project directory '{project_directory}' not found.")
        sys.exit(1)

    find_and_add_csproj_files(solution_path, project_directory)


# why doesnt join() work.
# read on ospath
# how does cecking for a specific file work
# how to chekc if file is .csproj exten
# why are sln files virutual!!!!!!!!!!!!!!!!!!!!
