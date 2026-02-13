# How to Fix "Updates were rejected"

This error happens because your GitHub repository already has some files (like a default README) that are not on your computer.

Since you want your computer's version to be the "correct" one, you should **force overwrite** the GitHub version.

Run this command in your terminal:

```bash
git push -f origin main
```

**Warning**: This deletes any files on GitHub that are not on your computer. Since this is a new upload, that is exactly what you want.
