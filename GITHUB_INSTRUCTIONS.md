# How to Push to GitHub

I have already initialized a local Git repository for you and committed all your files.

## Step 1: Create a Repository on GitHub
1.  Log in to your GitHub account.
2.  Click the **+** icon in the top right and select **New repository**.
3.  Name it `Anemia-Detection-CNN` (or whatever you like).
4.  **Do not** check "Initialize with README", "Add .gitignore", or "Add license" (since I already created these for you).
5.  Click **Create repository**.

## Step 2: Push Your Code
Once the repository is created, you will see a "Quick setup" page. Copy the URL (e.g., `https://github.com/YourUsername/Anemia-Detection-CNN.git`).

Then, open your terminal in this folder (`c:\Users\student\Desktop\CNN`) and run these two commands:

```bash
git remote add origin YOUR_GITHUB_URL_HERE
git branch -M main
git push -u origin main
```

*(Replace `YOUR_GITHUB_URL_HERE` with the link you copied from GitHub)*

## Done!
Refresh your GitHub page, and you will see all your files, including the README, source code, and models.
