# .gif	Graphics Interchange Format (GIF)	image/gif
# .jpeg, .jpg	JPEG images	image/jpeg
# .png	Portable Network Graphics	image/png
# .pdf	Adobe Portable Document Format (PDF)	application/pdf
# .txt	Text, (generally ASCII or ISO 8859-n)	text/plain
# .zip	ZIP archive	application/zip
# application/octet-stream

file = input("File name: ").strip().lower()

match file[file.rfind("."):]:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
