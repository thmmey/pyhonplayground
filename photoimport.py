import os

def fileIsMovie(p_filename):
    filename=str(p_filename)
    return filename.endswith("mp4")  or filename.endswith("MP4") or filename.endswith("MTS")


def fileIsPicture(p_filename):
    filename=str(p_filename)
    return filename.endswith("jpg")  or filename.endswith("JPG")

path = "H:" + os.sep + "PhotoImport"


albums = 0
with os.scandir(path) as it_outer:
    for entry_outer in it_outer:
        album = str(entry_outer.name)
        if not album.startswith('.') and entry_outer.is_dir():
            albums = albums + 1
            dir = path + os.sep + album
            files = 0
            pictures = 0
            videos = 0
            with os.scandir(dir) as it_inner:
                for entry_inner in it_inner:
                    if entry_inner.is_file():
                        filename = str(entry_inner.name).replace("'", "")
                        # Ohne Zählung überspringen
                        if filename == "Thumbs.db" or filename[0] == ".":
                            continue
                        files = files + 1
                        if fileIsPicture(filename):
                            pictures = pictures + 1
                        else:
                            if fileIsMovie(filename):
                                videos = videos + 1
                            else: 
                                print("unbekanntes file {0:s}".format(filename))
                        
               
                    if entry_inner.is_dir():
                        print("Directory " + entry_inner.name + " gefunden");

                result = "OK"
                if((videos + pictures) != files):
                    result = "!!"

                print("Album: {0:60s} files: {1:3d}, Bilder: {2:3d} Videos: {3:2d} --> {4:2s}".format(
                        entry_outer.name, files, pictures, videos, result))

             

print("Anzahl albums: {0:4d} ".format(albums))



