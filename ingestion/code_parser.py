import os

def load_code_files(repo_path):
    docs=[]

    for root, dirs, files in os.walk(repo_path):

        for file in files:
            if file.endswith(('.py', '.js', '.tsx', '.jsx', '.ipynb', '.java',
                       '.cpp', '.ts', '.go', '.rs', '.vue', '.swift', '.c', '.h')):
                
                file_path=os.path.join(root,file)

                with open(file_path,"r",encoding="utf-8") as f:

                    docs.append({
                        "content":f.read(),
                        "source":file_path
                    })

    return docs
            

