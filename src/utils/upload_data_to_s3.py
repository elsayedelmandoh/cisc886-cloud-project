import boto3
from huggingface_hub import HfApi, hf_hub_url
import requests
from src.config.settings import HF_TOKEN, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN, BUCKET_NAME, REGION, REPO_ID

api = HfApi(token=HF_TOKEN) 
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=REGION
)


print(f"Fetching file list from {REPO_ID}...")

all_files = [f for f in api.list_repo_files(repo_id=REPO_ID, repo_type="dataset") 
             if f.endswith(".parquet")]

print(f"Found {len(all_files)} files. Starting transfer to S3...")


for filename in all_files:
    
    s3_key = f"smol_ids_data/{filename.split('/')[-1]}"
    
    url = hf_hub_url(repo_id=REPO_ID, filename=filename, repo_type="dataset")
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    
    try:
        
        with requests.get(url, headers=headers, stream=True) as r:
            r.raise_for_status()
            s3_client.upload_fileobj(r.raw, BUCKET_NAME, s3_key)
            print(f" Done: {filename}")
    except Exception as e:
        print(f" Error in {filename}: {e}")

print("\n All files are now in your S3 bucket!")
