# what to submit

## Section 4 - Data Preprocessing with Apache Spark on EMR (5 marks)

### Code

1. **PySpark script or notebook** committed to GitHub with:
   - Inline comments explaining each step
   - Data loading from S3
   - Filtering and cleaning logic
   - Train/validation/test split
   - Output to S3

### Screenshots

2. **EMR console screenshot** showing cluster configuration (instance type, nodes, region)

3. **EMR console screenshot** showing cluster in **Terminated state** (REQUIRED)

4. **S3 screenshot** showing preprocessed output files 

### Report Content

5. **EMR cluster configuration table** documenting:
   - Cluster name
   - Instance type and node count
   - Region
   - Release and applications

6. **EDA figures** (at least 3) with captions:
   - Token length distribution histogram
   - Language/label distribution (pie/bar chart)
   - Sample count per split bar chart

> The teardown screenshot is REQUIRED. A missing teardown screenshot will be treated as an incomplete submission. EMR clusters left running deplete the shared account.

