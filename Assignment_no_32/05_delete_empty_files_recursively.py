import os

def delete_empty_files(path):
    if not os.path.isdir(path):
        print("Directory does not exist.")
        return

    deleted=0
    errors=0
    for root,dirs,files in os.walk(path):
        for name in files:
            file_path=os.path.join(root,name)
            try:
                if os.path.getsize(file_path)==0:
                    try:
                        os.remove(file_path)
                        deleted+=1
                        print("Deleted:",file_path)
                    except (PermissionError,OSError) as e:
                        errors+=1
                        print(f"Could not delete {file_path}: {e}")
            except (PermissionError,OSError) as e:
                errors+=1
                print(f"Could not check {file_path}: {e}")

    print(f"Empty files deleted: {deleted}")
    print(f"Errors encountered: {errors}")

path=input("Enter directory path: ").strip()
delete_empty_files(path)
