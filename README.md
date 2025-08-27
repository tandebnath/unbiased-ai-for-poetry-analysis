# Setup Instructions

This repository contains various worksets for the "Unbiased AI for Poetry Analysis" project.

## Repository Structure

A sample layout has been explained below:

- `pilot_study_worksets/`
  - `workset1_100_poems/`
    - `workset1_generation_script.py`
    - `annotation.csv` *(empty placeholder — for saving your annotations)*
    - `notes.csv` *(empty placeholder — for saving notes on volumes)*
  - `workset2_100_poems/`
  - `workset3_100_poems/`
- `full_corpus_ids.txt` *(list of all 120 volume IDs in the dataset)*

---

### Step 1: Download the Full Corpus via HTRC

Use the `full_corpus_ids.txt` file to download the entire dataset into your secure volume.

```bash
htrc download full_corpus_ids.txt -o /media/secure_volume/full_corpus
```
This will create a directory:
```
full_corpus
```
containing all volumes listed in full_corpus_ids.txt.
For more information about the htrc download command and optional flags, see the [HTRC documentation](https://htrc.github.io/HTRC-WorksetToolkit/cli.html).

### Step 2: Prepare Your Workset

1. Navigate to your assigned workset folder (e.g., workset1_100_poems).
2. Ensure the following files are present in that folder:
	•	workset1_generation_script.py
	•	annotation.csv
	•	notes.csv
	•	The full_corpus/ directory downloaded in Step 1
3. Run the generation script for your workset:
```bash
python workset1_generation_script.py
```

### Step 3. Verify Output

Running the script in Step 2 will generate a new directory:
```
workset1/collection/
```
This is the working directory for the annotation tool. All assigned poem files will be copied here.

### Step 4. Begin Annotating!

- Run the annotation tool pointing it to your generated worksetX/collections/ folder.
- Use annotation.csv to record your annotations.
- Use notes.csv to save any observations about volumes or OCR issues.

--- 

### Support

If you encounter any issues, please reach out at: tand3@illinois.edu


