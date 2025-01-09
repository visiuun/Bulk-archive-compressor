# Archive Compression Utility

This Python script allows you to compress files and directories into ZIP format. It offers two modes of compression:
1. **All files into one ZIP file**: Compresses all files from the selected folder into a single ZIP archive.
2. **Separate files into individual ZIP files**: Compresses each file from the selected folder into its own separate ZIP archive.

The script utilizes multithreading to process files efficiently, providing faster performance when compressing multiple files.

## Requirements

This script requires Python 3.x and the following modules:
- `os`
- `zipfile`
- `tkinter` (for GUI file/folder selection)
- `pathlib`
- `threading`

No additional external packages need to be installed, as all dependencies are part of the standard Python library.

## Features

- **Compression Modes**: You can choose to compress all files into a single ZIP file or compress each file into its own ZIP archive.
- **Multithreading**: The script uses Python's threading library to compress files concurrently, speeding up the process when dealing with multiple files.
- **Graphical User Interface (GUI)**: A user-friendly interface is provided for selecting input and output folders using Tkinter's file dialog.

## Usage Instructions

1. **Running the Script**:
   - Simply run the script. It will open a file dialog for you to select the input folder containing the files you wish to compress.
   - After selecting the input folder, you'll be prompted to select an output folder where the compressed archives will be saved.
   - Then, choose whether you want to compress all files into one ZIP file or each file into a separate ZIP file.

2. **Compression Process**:
   - If you choose to compress all files into one ZIP, a single ZIP archive named `all_files.zip` will be created in the output folder.
   - If you choose to compress each file separately, individual ZIP files will be created for each file, retaining the original directory structure.

## How It Works

### Functions:

1. **`compress_file(file_path, relative_path, output_folder)`**:
   - Compresses an individual file into the corresponding ZIP file, ensuring that the folder structure is preserved.
   
2. **`compress_to_zip(input_folder, output_folder, zip_all=False)`**:
   - Collects all files in the input folder and compresses them either into one ZIP file or separate ZIP files.
   - Uses multithreading to speed up compression when compressing individual files.
   
3. **`select_folders()`**:
   - Prompts the user to select input and output folders using file dialogs.
   - Asks the user whether they want to compress files into one archive or separate ones.

### Flow:
- The script starts by asking the user to select the input folder containing files to compress.
- It then asks for the output folder.
- The user is prompted to choose whether to compress all files into a single ZIP file or separate them.
- Files are processed, and the selected mode of compression is executed.

### Sample Usage:

1. Run the script:
   ```bash
   python "Bulk zip compressor.py"
   ```

2. Follow the prompts to select the input folder and output folder.

3. The script will display a confirmation message once the compression is complete.

## Error Handling

- The script checks if the input or output folder is not selected and provides a message to inform the user.
- If any issues arise during the compression process, an error message will appear, and the script will notify the user of the specific problem.

## Notes

- Ensure that the input folder does not contain any nested archives, as this script only handles files and folders.
- The multithreading approach improves performance when compressing large numbers of files.
