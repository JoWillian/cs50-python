def main():
    ext = input("File name: ").strip().lower()
    if ext[-3:] == "gif":
        print("image/gif")
    elif ext[-3:] == "jpg" or ext[-4:] == "jpeg":
        print("image/jpeg")
    elif ext[-3:] == "pdf":
        print("application/pdf")
    elif ext[-3:] == "png":
        print("image/png")
    elif ext[-3:] == "zip":
        print("application/zip")
    elif ext[-3:] == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()
