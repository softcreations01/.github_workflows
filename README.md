# GitHub Action Workflow

This GitHub Action workflow can be used to run your tests on a self-hosted runner or an Ubuntu-latest runner.

# Prerequisites

   + A GitHub repository
    + A self-hosted runner or github hosted runners

# Usage

To use this workflow, you will need to follow these steps:

  - Fork, clone and star this repository
   - For Github Hosted Runners:
            
     Open the folder named .github/workflows/main.yml in this GitHub repository. 
         Change the content in the file named first-actions.yml for runs-on as follows:

    runs-on: ubuntu-latest

  Commit the .github/workflows/main.yml file to your GitHub repository.
    Push the changes to your GitHub repository.

- For Self-Hosted Runners:

  Open the folder named .github/workflows/main.yml in this GitHub repository. 
         Change the content in the file named first-actions.yml for runs-on as follows:

        runs-on: self-hosted

    Commit the .github/workflows/main.yml file to your GitHub repository.
    Push the changes to your GitHub repository.

The workflow will now run whenever you push changes to the main branch of your repository.

# Troubleshooting

If you encounter any problems, please refer to the GitHub Actions documentation for help.

# Additional Notes

  This workflow is just an example, and you may need to modify it to fit your specific needs.
    For more information on GitHub Actions, please visit the GitHub Actions website: https://github.com/features/actions
