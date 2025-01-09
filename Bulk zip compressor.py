import os
import zipfile
from pathlib import Path
from tkinter import Tk, filedialog, messagebox
import threading

def compress_file(file_path, relative_path, output_folder):
    """Compress individual file into the corresponding ZIP file"""
    zip_file_path = Path(output_folder) / f"{relative_path.parent}.zip"
    
    # Ensure the output directory for the zip file exists
    zip_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create or append to the ZIP file
    with zipfile.ZipFile(zip_file_path, 'a', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=relative_path)
        print(f"Added {file_path} to {zip_file_path}")

def compress_to_zip(input_folder, output_folder, zip_all=False):
    """Compress files into ZIP, either all into one or separate files"""
    files_to_zip = []

    # Collect all files to zip
    for root, _, files in os.walk(input_folder):
        for file in files:
            file_path = Path(root) / file
            relative_path = file_path.relative_to(input_folder)
            files_to_zip.append((file_path, relative_path))

    if zip_all:
        # Create one large ZIP file containing all files
        zip_file_path = Path(output_folder) / f"all_files.zip"
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path, relative_path in files_to_zip:
                zipf.write(file_path, arcname=relative_path)
                print(f"Added {file_path} to {zip_file_path}")
        messagebox.showinfo("Compression Completed", f"All files compressed into {zip_file_path}")
    else:
        # Use threading to compress files in parallel
        threads = []
        for file_path, relative_path in files_to_zip:
            # Create and start a new thread for each file
            thread = threading.Thread(target=compress_file, args=(file_path, relative_path, output_folder))
            thread.start()
            threads.append(thread)
        
        # Wait for all threads to finish
        for thread in threads:
            thread.join()
        
        messagebox.showinfo("Compression Completed", "Files compressed into separate ZIP files.")

def select_folders():
    """Prompt user to select folders and start compression"""
    root = Tk()
    root.withdraw()  # Hide the root window
    
    # Prompt user to select the input folder
    input_folder = filedialog.askdirectory(title="Select the input folder")
    if not input_folder:
        print("No input folder selected. Exiting...")
        messagebox.showinfo("No Input Folder", "No input folder selected. Exiting...")
        return
    
    # Prompt user to select the output folder
    output_folder = filedialog.askdirectory(title="Select the output folder")
    if not output_folder:
        print("No output folder selected. Exiting...")
        messagebox.showinfo("No Output Folder", "No output folder selected. Exiting...")
        return

    # Ask user if they want to zip all files into one ZIP or separate by folder
    zip_all = messagebox.askyesno(
        title="Select Compression Mode",
        message="Do you want to compress all files into one ZIP file?"
    )
    
    # Start compressing files and folders to ZIP
    compress_to_zip(input_folder, output_folder, zip_all)

# Run the folder selection and compression process
if __name__ == "__main__":
    select_folders()