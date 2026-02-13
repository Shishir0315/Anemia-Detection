# How to Run Your Model in a Hugging Face Space

I have configured your project to run as a **Docker Space** on Hugging Face. This will allow you to see and use your web app directly in the browser.

## Step 1: Create a Space on Hugging Face
1.  Go to [huggingface.co/new-space](https://huggingface.co/new-space).
2.  Set the **Space Name** to `Anemia-Detection-App`.
3.  **Select the SDK**: Choose **Docker**.
4.  Set the Space to **Public**.
5.  Click **Create Space**.

## Step 2: Push Your Code to the Space
1. Open your terminal in `c:\Users\student\Desktop\CNN`.
2. Add the Space as a new git remote:
   ```bash
   git remote add space https://huggingface.co/spaces/Shishir0315/Anemia-Detection-App
   ```
3. Push your code to the Space:
   ```bash
   git push -f space main
   ```

## Step 3: Wait for Building
Hugging Face will now see your `Dockerfile` and start building the container.
- It will take 2-3 minutes to install the libraries (TensorFlow, Flask, etc.).
- Once finished, you will see your **"Anemia AI" web interface** running directly in the browser on your Hugging Face Space page!

---

**Note**: I have updated `app.py` to use port **7860**, which is what Hugging Face expects.
