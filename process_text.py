import glob
import textract

#For each file in folder, read file
#text = textract.process(path+filename)
#text.decode(encoding="utf-8", errors="ignore")

def get_text(globpath):
    textdict = {}
    for filepath in glob.glob(globpath):
        try:
            text = textract.process(filepath).decode(encoding="utf-8", errors="ignore")
            textdict[filepath] = text
        except Exception as e:
            textdict[filepath] = f"{e} at {filepath}"
    return textdict

#    104/2294 return with an error from D:\JWbackup\私人活儿\传神\*.doc

#Extract text to Translation.csv
#probably split on \n\n, extract evens to one column and odds to another?
# Remember to join all chinese and English in one file
