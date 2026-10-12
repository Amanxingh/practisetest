# Python Task Manager

A beginner-friendly command-line Python project. It lets you add tasks, view them, mark them complete, and delete them. Tasks are saved in `tasks.json`, so they remain after you close the program.

## Requirements
- Python 3.10 or newer
- Visual Studio Code
- The Microsoft Python extension in VS Code (recommended)

## Run in VS Code

1. Extract `python_task_manager.zip`.
2. Open VS Code.
3. Select **File → Open Folder** and open the extracted `python_task_manager` folder.
4. Open **Terminal → New Terminal**.
5. Run:

   ```bash
   python --version
   ```

   If that command is not recognized on Windows, try `py --version`.

6. Start the program:

   ```bash
   python app.py
   ```

   If needed on Windows, use:

   ```powershell
   py app.py
   ```

## How to use
- Choose `1` to view tasks.
- Choose `2` to add a task.
- Choose `3` to mark a task as complete.
- Choose `4` to delete a task.
- Choose `5` to exit.

## Project structure

```text
python_task_manager/
├── app.py
├── tasks.json
├── requirements.txt
└── README.md
```

This project uses only Python's standard library, so no `pip install` step is required.
