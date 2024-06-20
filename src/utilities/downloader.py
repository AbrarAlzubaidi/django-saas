import requests
from pathlib import Path

def download_file(url:str, file_path:Path, parent_mkdir:bool=True):
    """
    url: the url static file that want to be downloaded
    file_path: what is the file path of the url that want to download
    parent_mkdir: if the parent directory is exist (in this situation the staticfiles/vendor) then append the file_name to it
    """
    # these the below setups to make sure that the "staticfiles/vendor" folders are exists so we can add the files to them 
    if not isinstance(file_path, Path):
        raise ValueError(f'{file_path} mus be a valid Path object')
    if parent_mkdir: # if the parent directory flag is true then create the destination file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # parents=True: Creates all parent directories in the path if they do not exist.
        # exist_ok=True: Does not raise an error if the directory already exists.
    
    # the setups below is for getting the content from the url and write it into the file that been created.
    try:
        response = requests.get(url)
        # if the response is failed then raise error
        response.raise_for_status()
        # if the response not failed then write the content of the url into the file_name
        file_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"the url: {url}  not downloaded successfully")
        return False
